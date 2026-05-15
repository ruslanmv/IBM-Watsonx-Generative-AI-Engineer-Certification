#!/bin/bash

echo "Building IBM C1000-185 Study Guide..."

# Clean previous builds
rm -f main.pdf main.aux main.log main.toc main.lof main.lot main.out main.bbl main.blg

# First pass
echo "First LaTeX pass..."
pdflatex -interaction=nonstopmode main.tex

# Bibliography
echo "Processing bibliography..."
bibtex main

# Second pass
echo "Second LaTeX pass..."
pdflatex -interaction=nonstopmode main.tex

# Third pass (for references)
echo "Third LaTeX pass..."
pdflatex -interaction=nonstopmode main.tex

# Check if PDF was created
if [ -f main.pdf ]; then
    echo "✓ Build successful! PDF created: main.pdf"
    echo "File size: $(du -h main.pdf | cut -f1)"
else
    echo "✗ Build failed. Check the log files for errors."
    exit 1
fi

# Optional: Clean auxiliary files
read -p "Clean auxiliary files? (y/n) " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    rm -f main.aux main.log main.toc main.lof main.lot main.out main.bbl main.blg
    echo "✓ Cleaned auxiliary files"
fi
