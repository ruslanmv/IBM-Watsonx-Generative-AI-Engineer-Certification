#!/usr/bin/env bash
#
# Non-interactive LaTeX build for the C1000-185 study guide.
# Default target = KDP letter (8.5" x 11") trim.
# For the 6" x 9" print run:  ./build.sh print
#
# Requirements:
#   * TeX Live or MiKTeX with biblatex + biber/bibtex
#   * No -shell-escape needed (we do NOT use the `minted` package)
#
set -euo pipefail

SIZE="${1:-kdp}"          # 'kdp' (letter) | 'print' (6x9)
JOB="main"
LATEX_OPTS="-interaction=nonstopmode -halt-on-error -file-line-error"

echo "→ Building IBM C1000-185 Study Guide  (size=${SIZE})"

# Clean previous artefacts
rm -f ${JOB}.pdf ${JOB}.aux ${JOB}.log ${JOB}.toc ${JOB}.lof ${JOB}.lot \
      ${JOB}.out ${JOB}.bbl ${JOB}.blg ${JOB}.bcf ${JOB}.run.xml

# Render the requested size by setting \BookSize before \input{main}
render() {
    pdflatex ${LATEX_OPTS} "\\def\\BookSize{${SIZE}}\\input{${JOB}}"
}

echo "→ pdflatex pass 1"
render

echo "→ bibtex"
bibtex ${JOB} || true   # tolerate no-citations on first run

echo "→ pdflatex pass 2"
render

echo "→ pdflatex pass 3 (resolves cross-refs and TOC)"
render

if [ -f "${JOB}.pdf" ]; then
    echo "✓ Build succeeded → ${JOB}.pdf  ($(du -h ${JOB}.pdf | cut -f1))"
else
    echo "✗ Build failed — see ${JOB}.log"
    exit 1
fi
