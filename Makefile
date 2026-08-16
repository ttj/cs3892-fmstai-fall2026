# Course document build.
#
#   make pdf     regenerate syllabus/syllabus.pdf from syllabus/syllabus.md
#   make links   re-check every URL in the repo (writes link-check.txt, gitignored)
#
# Pipeline: pandoc (GitHub-flavoured markdown) -> standalone HTML with inlined print CSS
#           -> headless Chrome --print-to-pdf.
# Rationale: pandoc's LaTeX writer chokes on some of the unicode and long URLs here, and
# Chrome's print engine gives usable page breaks and clickable links without a TeX install.

PANDOC  ?= pandoc
CHROME  ?= $(shell command -v google-chrome || command -v chromium || command -v chromium-browser)

.PHONY: pdf links clean

pdf: syllabus/syllabus.pdf

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
	@echo "wrote $@"

links:
	@grep -rhoE 'https?://[^ )>,"`]+' --include='*.md' . \
	  | sed 's/[.,;:]$$//' | sort -u > .links.txt
	@echo "$$(wc -l < .links.txt) unique URLs; checking..."
	@while read -r u; do \
	  code=$$(curl -sS -o /dev/null -w '%{http_code}' -L --max-time 30 \
	    -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/140.0 Safari/537.36' "$$u"); \
	  printf '%-6s %s\n' "$$code" "$$u"; \
	done < .links.txt | tee link-check.txt | grep -v '^200' || true
	@rm -f .links.txt
	@echo "full results in link-check.txt (see LINK-AUDIT.md for known bot-blocked hosts)"

clean:
	rm -rf .pandoc-tmp .links.txt link-check.txt
