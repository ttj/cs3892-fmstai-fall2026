# Course document build.
#
#   make pdf     regenerate syllabus/syllabus.pdf and assignments/hw*.pdf from their .md sources
#   make links   re-check every URL in the repo (writes link-check.txt, gitignored)
#   make student-links   every link a student can click opens for a student (markdown and PDFs)
#
# Pipeline: pandoc (GitHub-flavoured markdown) -> standalone HTML with inlined print CSS
#           -> headless Chrome --print-to-pdf.
# Rationale: pandoc's LaTeX writer chokes on some of the unicode and long URLs here, and
# Chrome's print engine gives usable page breaks and clickable links without a TeX install.
#
# tools/abs-links.lua turns repository-relative links into absolute GitHub URLs. Without it a
# link from one document to another becomes file:///... on the build machine, dead for students.

PANDOC  ?= pandoc
CHROME  ?= $(shell command -v google-chrome || command -v chromium || command -v chromium-browser)

.PHONY: check pdf links student-links clean

## check: validate every cross-referenced fact against course.yml, and that
## nothing instructor-only has leaked into this class-facing repo.
check:
	@python3 -c "import yaml" 2>/dev/null || pip install --quiet pyyaml
	@python3 scripts/check_course.py

pdf: syllabus/syllabus.pdf assignments/hw1.pdf assignments/hw2.pdf assignments/hw3.pdf assignments/hw4.pdf assignments/hw5.pdf

syllabus/syllabus.pdf: syllabus/syllabus.md tools/print.css tools/abs-links.lua
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="CS 3892/5892 — Formal Methods: Safe and Trustworthy AI — Fall 2026" \
	  --css tools/print.css --embed-resources \
	  --lua-filter tools/abs-links.lua -M srcdir=syllabus \
	  -o .pandoc-tmp/syllabus.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/syllabus.html
	@rm -rf .pandoc-tmp
	@# Stamp the source hash. git does not preserve mtimes, so this is what
	@# lets CI tell a stale committed PDF from a fresh one.
	@sha256sum syllabus/syllabus.md | cut -d' ' -f1 > syllabus/.syllabus.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw1.pdf: assignments/hw1.md tools/print.css tools/abs-links.lua $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	@# --resource-path lets `figures/x.svg` in the markdown resolve both here and on
	@# GitHub, which reads it relative to the .md file. --embed-resources then inlines
	@# it, so the Chrome step needs no path of its own.
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW1 — Logic, SAT/SMT, and bounded reachability — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  --lua-filter tools/abs-links.lua -M srcdir=assignments \
	  -o .pandoc-tmp/hw1.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw1.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw1.md | cut -d' ' -f1 > assignments/.hw1.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw2.pdf: assignments/hw2.md tools/print.css tools/abs-links.lua $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW2 — Temporal logic and model checking — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  --lua-filter tools/abs-links.lua -M srcdir=assignments \
	  -o .pandoc-tmp/hw2.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw2.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw2.md | cut -d' ' -f1 > assignments/.hw2.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw3.pdf: assignments/hw3.md tools/print.css tools/abs-links.lua $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW3 — Program analysis — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  --lua-filter tools/abs-links.lua -M srcdir=assignments \
	  -o .pandoc-tmp/hw3.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw3.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw3.md | cut -d' ' -f1 > assignments/.hw3.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw4.pdf: assignments/hw4.md tools/print.css tools/abs-links.lua $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW4 — Interactive theorem proving in Lean 4 — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  --lua-filter tools/abs-links.lua -M srcdir=assignments \
	  -o .pandoc-tmp/hw4.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw4.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw4.md | cut -d' ' -f1 > assignments/.hw4.md.sha256
	@echo "wrote $@ (+ source stamp)"

assignments/hw5.pdf: assignments/hw5.md tools/print.css tools/abs-links.lua $(wildcard assignments/figures/*)
	@mkdir -p .pandoc-tmp
	$(PANDOC) -f gfm -t html5 --standalone \
	  --metadata pagetitle="HW5 — Neural-network verification — CS 3892/5892" \
	  --css tools/print.css --embed-resources --resource-path=.:assignments \
	  --lua-filter tools/abs-links.lua -M srcdir=assignments \
	  -o .pandoc-tmp/hw5.html $<
	$(CHROME) --headless=new --disable-gpu --no-sandbox \
	  --no-pdf-header-footer --print-to-pdf=$@ \
	  file://$(CURDIR)/.pandoc-tmp/hw5.html
	@rm -rf .pandoc-tmp
	@sha256sum assignments/hw5.md | cut -d' ' -f1 > assignments/.hw5.md.sha256
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

## student-links: no file: links, no missing files, and every link into a GitHub
## repository goes to a PUBLIC repository and a path that exists. The script lives
## in the examples repository; use the checkout beside this one, or fetch it.
STUDENT_LINKS := $(firstword $(wildcard ../cs3892-examples/scripts/check_links.py))
student-links:
ifeq ($(STUDENT_LINKS),)
	@curl -sSfL https://raw.githubusercontent.com/ttj/cs3892-examples/main/scripts/check_links.py -o .check_links.py
	@python3 .check_links.py --skip LINK-AUDIT.md . ; rc=$$?; rm -f .check_links.py; exit $$rc
else
	@python3 $(STUDENT_LINKS) --skip LINK-AUDIT.md .
endif

clean:
	rm -rf .pandoc-tmp .links.txt link-check.txt
