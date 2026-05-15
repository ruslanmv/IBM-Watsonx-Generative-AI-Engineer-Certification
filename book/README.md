# LaTeX Study Guide — build &amp; publish

LaTeX source for the **IBM watsonx Generative AI Engineer Associate (C1000-185)** study guide. Build a PDF locally and ship it to Amazon KDP, Lulu, or any print-on-demand service.

## What is in this directory

```
book/
  main.tex                       master document; configures geometry, fonts, colour boxes
  build.sh                       non-interactive build script (kdp | print)
  Makefile                       targets: book, kdp, print, watch, clean, distclean
  .gitignore                     keeps build artefacts out of git
  cover/                         KDP cover spec + template
  bibliography/references.bib    BiBLaTeX entries cited in the book
  chapters/
    00-frontmatter.tex           title, copyright, TOC, preface, study plan
    ch01-foundations.tex         Section 1 — Analyze &amp; Design (15%)
    ch02-prompt-engineering.tex  Section 2 — Prompt Engineering (16%)
    ch03-fine-tuning.tex         Section 3 — Fine-Tuning (31% ★)
    ch04-rag.tex                 Section 4 — RAG (17%)
    ch05-deployment.tex          Section 5 — Deployment (13%)
    ch06-integration.tex         Section 6 — Integration &amp; Orchestration (8%)
    99-backmatter.tex            conclusion + About the Author + Also by
    appendix-a-glossary.tex      glossary (60+ terms)
    appendix-b-mock-exam.tex     40-question mock exam
    appendix-c-answers.tex       answer key with chapter references
    appendix-d-cheatsheet.tex    one-page exam cheat sheet
```

## Requirements

A TeX distribution with `pdflatex`, `bibtex`, and the packages used by `main.tex` (all on TeX Live full):

```bash
# Ubuntu / Debian
sudo apt-get install -y texlive-full

# macOS (Homebrew)
brew install --cask mactex-no-gui

# Windows
# https://miktex.org/download   (then run the package wizard)
```

No `-shell-escape` is needed; the source uses `listings`, not `minted`.

## Build

```bash
cd book
./build.sh                # default: 8.5" x 11" letter (KDP digital / Kindle)
./build.sh print          # 6" x 9" trim paperback (KDP print-on-demand)
```

or via Make:

```bash
make          # same as 'make kdp'
make print    # 6x9 paperback variant
make watch    # auto-rebuild on save (needs latexmk)
make clean    # remove aux files
make distclean# also remove the PDF
```

The output is `main.pdf`. The build runs `pdflatex → bibtex → pdflatex → pdflatex` so cross-references, the TOC, and the bibliography all resolve in one go.

## Build in Overleaf

1. Create a new Overleaf project, upload the entire `book/` folder.
2. **Menu → Settings → Compiler:** `pdfLaTeX`.
3. **TeX Live version:** 2024 or newer.
4. Click *Recompile*.

Overleaf does not need `-shell-escape`; the project compiles out of the box.

## Build in CI (GitHub Actions)

The repository ships a workflow at `.github/workflows/build-book.yml` that runs on every push and on tags. It produces `main.pdf` as a build artefact and attaches it to releases. Trigger manually from the *Actions* tab too.

## Publishing to Amazon KDP

KDP accepts two distinct files: the **manuscript** PDF and the **cover** PDF/JPG.

### 1. Manuscript

* **Digital / Kindle eBook:** use `./build.sh` (letter trim). Upload `main.pdf` as the manuscript when listing a Kindle eBook — KDP converts it.
* **Paperback (print-on-demand):** use `./build.sh print` for a 6" x 9" trim with KDP-compliant inner / outer margins. Confirm the page count, then size the cover accordingly.

### 2. ISBN

KDP can assign a free ISBN, or you can use your own. Add it to the copyright page in `chapters/00-frontmatter.tex` (search for `ISBN:`) before generating the print PDF.

### 3. Cover

See `cover/README.md` for the exact pixel dimensions, bleed, and spine width by page count, plus a template recommendation.

### 4. Pre-publication checklist

- [ ] Replace `ISBN: [To be assigned]` in `chapters/00-frontmatter.tex`.
- [ ] Re-build and skim the PDF page by page (no `??`, no orphan headings).
- [ ] Validate the cover at the size shown by KDP after upload.
- [ ] Set the categories and keywords (suggested: *generative AI, certification, IBM, watsonx, LLM*).
- [ ] Set the price (`$24.99` for the paperback is a typical reference point for a 300-page technical study guide).
- [ ] Order an author proof and review printed sharpness, gutter margins, and front-cover colours.

## License

The contents of this `book/` directory are licensed under the **Apache License, Version 2.0** — see the root [LICENSE](../LICENSE) file. You may republish, translate, and adapt the material under those terms; attribution to *Ruslan Idelfonso Magana Vsevolodovna · ruslanmv.com* is appreciated.
