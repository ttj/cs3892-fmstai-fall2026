# Course document build.
#
#   make pdf     regenerate syllabus/syllabus.pdf and assignments/hw*.pdf from their .md sources
#   make links   re-check every URL in the repo (writes link-check.txt, gitignored)
#
# Pipeline: pandoc (GitHub-flavoured markdown) -> standalone HTML with inlined print CSS
#           -> headless Chrome --print-to-pdf.
# Rationale: pandoc's LaTeX writer chokes on some of the unicode and long URLs here, and
# Chrome's print engine gives usable page breaks and clickable links without a TeX install.

PANDOC  ?= pandoc
CHROME  ?= $(shell command -v google-chrome || command -v chromium || command -v chromium-browser)

.PHONY: check pdf links clean

## check: validate every cross-referenced fact against course.yml, and that
## nothing instructor-only has leaked into this class-facing repo.
check:
	@python3 -c "import yaml" 2>/dev/null || pip install --quiet pyyaml
	@python3 scripts/check_course.py

pdf: syllabus/syllabus.pdf assignments/hw1.pdf assignments/hw2.pdf

syllabus/syllabus.pdf: syllabus/syllabus.md tools/print.css
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="CS 3892/5892 — Formal Methods: Safe and Trustworthy AI — Fall 2026" \
	  --css tools/print.css --embed-resources \
	  -o .pandoc-tmp/syllabus.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/syllabus.html
	@rm -rf .pandoc-tmp
	@# Stamp the source hash. git does not preserve mtimes, so this is what
	@# lets CI tell a stale committed PDF from a fresh one.
	@sha256sum syllabus/syllabus.md | cut -d' ' -f1 > syllabus/.syllabus.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw1.pdf: assignments/hw1.md tools/print.css $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	@# --resource-path lets `figures/x.svg` in the markdown resolve both here and on
	@# GitHub, which reads it relative to the .md file. --embed-resources then inlines
	@# it, so the Chrome step needs no path of its own.
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW1 — Logic, SAT/SMT, and bounded reachability — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  -o .pandoc-tmp/hw1.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw1.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw1.md | cut -d' ' -f1 > assignments/.hw1.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw2.pdf: assignments/hw2.md tools/print.css $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW2 — Temporal logic and model checking — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  -o .pandoc-tmp/hw2.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw2.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw2.md | cut -d' ' -f1 > assignments/.hw2.md.sha256
	@echo "wrote $@ (+ source stamp)"

links:
	@grep -rhoE 'https?://[^ )>"`]+' --include='*.md' . \
	  | sed -E 's/[.,;:]+$$//' | sort -u > .links.txt
	@echo "$$(wc -l < .links.txt) unique URLs; checking..."
	@while read -r u; do \
	  code=$$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 30 \
	    -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140.0 Safari/537.36' "$$u"); \
	  printf '%-6s %s\n' "$$code" "$$u"; \
	  sleep 0.4; \
	done < .links.txt | tee link-check.txt | grep -vE '^(200|202|203) ' || true
	@rm -f .links.txt
	@echo "full results in link-check.txt (see LINK-AUDIT.md for known bot-blocked hosts)"

clean:
	rm -rf .pandoc-tmp .links.txt link-check.txt
