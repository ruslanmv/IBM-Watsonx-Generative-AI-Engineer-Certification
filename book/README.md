# LaTeX Study Guide

This directory contains the LaTeX source files for the IBM C1000-185 Study Guide.

## Structure

```
book/
├── main.tex                 # Main LaTeX document
├── chapters/                # Individual chapter files
├── images/                  # Figures and diagrams
├── styles/                  # Custom LaTeX styles
├── bibliography/            # BibTeX references
└── build.sh                # Build script
```

## Building the PDF

### Prerequisites

- TeX Live or MiKTeX distribution
- LaTeX packages: see main.tex for required packages

### Quick Build

```bash
./build.sh
```

### Manual Build

```bash
pdflatex main.tex
bibtex main
pdflatex main.tex
pdflatex main.tex
```

## Output

The compiled PDF will be `main.pdf` - suitable for:
- Amazon Kindle Direct Publishing (KDP)
- Print-on-demand services
- Digital distribution

## Customization

Edit `main.tex` to customize:
- Page geometry and margins
- Colors (IBM brand colors are pre-defined)
- Fonts and typography
- Header/footer styles
