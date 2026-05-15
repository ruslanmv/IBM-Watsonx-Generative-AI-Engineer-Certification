# ============================================================================
# Makefile for the C1000-185 study-guide LaTeX source.
# Produces a KDP-ready PDF without -shell-escape.
# ============================================================================

JOB        := main
LATEX_OPTS := -interaction=nonstopmode -halt-on-error -file-line-error

.PHONY: help book kdp print clean distclean watch

help: ## Show this help.
	@echo "Targets:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) \
		| awk 'BEGIN {FS = ":.*?## "}; {printf "  %-12s %s\n", $$1, $$2}'

book: kdp  ## Build the default (KDP letter) PDF.

kdp:        ## Build the 8.5"x11" letter PDF for KDP / digital distribution.
	@bash build.sh kdp

print:      ## Build the 6"x9" trim paperback PDF for KDP print-on-demand.
	@bash build.sh print

watch:      ## Auto-rebuild on file changes (requires latexmk).
	latexmk -pdf -pvc -interaction=nonstopmode $(JOB).tex

clean:      ## Remove auxiliary build files (keeps the PDF).
	rm -f $(JOB).aux $(JOB).log $(JOB).toc $(JOB).lof $(JOB).lot \
	      $(JOB).out $(JOB).bbl $(JOB).blg $(JOB).bcf $(JOB).run.xml \
	      $(JOB).synctex.gz $(JOB).fls $(JOB).fdb_latexmk

distclean: clean  ## Also remove main.pdf.
	rm -f $(JOB).pdf
