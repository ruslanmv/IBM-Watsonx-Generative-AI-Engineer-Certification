# ============================================================================
# Makefile for the C1000-185 study-guide LaTeX source.
# Produces a KDP-ready PDF without -shell-escape.
# ============================================================================

JOB        := main
LATEX_OPTS := -interaction=nonstopmode -halt-on-error -file-line-error

FIG_DIR    := assets/figures
SVGS       := $(wildcard $(FIG_DIR)/*.svg)
PDFS       := $(SVGS:.svg=.pdf)

.PHONY: help book kdp print clean distclean watch figures

help: ## Show this help.
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

book: figures kdp  ## Build figures, then the default (KDP letter) PDF.

figures: $(PDFS) ## Convert every assets/figures/*.svg to *.pdf.

$(FIG_DIR)/%.pdf: $(FIG_DIR)/%.svg
	@if command -v rsvg-convert >/dev/null 2>&1; then \
		rsvg-convert -f pdf -o $@ $< ; \
	elif command -v inkscape >/dev/null 2>&1; then \
		inkscape --export-type=pdf --export-filename=$@ $< ; \
	else \
		echo "ERROR: install rsvg-convert (librsvg) or inkscape to render SVG figures" ; \
		exit 1 ; \
	fi

kdp: figures ## Build the 8.5"x11" letter PDF for KDP / digital distribution.
	@bash build.sh kdp

print: figures ## Build the 6"x9" trim paperback PDF for KDP print-on-demand.
	@bash build.sh print

watch:      ## Auto-rebuild on file changes (requires latexmk).
	latexmk -pdf -pvc -interaction=nonstopmode $(JOB).tex

clean:      ## Remove auxiliary build files (keeps the PDF).
	rm -f $(JOB).aux $(JOB).log $(JOB).toc $(JOB).lof $(JOB).lot \
	      $(JOB).out $(JOB).bbl $(JOB).blg $(JOB).bcf $(JOB).run.xml \
	      $(JOB).synctex.gz $(JOB).fls $(JOB).fdb_latexmk

distclean: clean  ## Also remove main.pdf and generated figure PDFs.
	rm -f $(JOB).pdf $(PDFS)
