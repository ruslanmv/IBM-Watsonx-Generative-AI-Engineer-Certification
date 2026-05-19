# Book Figures

This folder holds the editable **SVG sources** for every figure in the study
guide, plus the **pre-rendered PDFs** that pdfLaTeX consumes.

## Layout

```
book/assets/figures/
├── fig01-exam-blueprint.svg         (editable source)
├── fig01-exam-blueprint.pdf         (auto-generated, included by LaTeX)
├── fig02-roadmap.svg
├── fig02-roadmap.pdf
└── …
```

## Style guide

| Element       | Spec |
|---------------|------|
| Background    | `#ffffff` (white, print-friendly) |
| Primary       | `#0072C6` (IBM blue) |
| Dark primary  | `#003865` (IBM dark blue) |
| Accent purple | `#8A3FFC` |
| Accent green  | `#009E60` |
| Accent red    | `#DA1E28` |
| Gray fills    | `#F0F0F0` / strokes `#525F6B` |
| Font          | `font-family="Helvetica, Arial, sans-serif"` |
| Stroke width  | 2px for primary lines, 1px for sub-lines |
| ViewBox       | typically `0 0 800 500` (matches book column ratio) |

## Regenerating the PDFs

Each SVG is converted to PDF before `pdflatex` runs. Use one of:

```bash
make figures            # uses rsvg-convert (preferred, faster)
# or
inkscape --export-type=pdf book/assets/figures/*.svg
```

The GitHub Actions build runs this step automatically.

## Authoring a new figure

1. Add `figXX-name.svg` here.
2. Keep the same palette / sans-serif font.
3. Run `make figures` locally (or just push — CI will render).
4. Reference from a chapter:

   ```latex
   \begin{figure}[h]
   \centering
   \includegraphics[width=0.85\textwidth]{assets/figures/figXX-name}
   \caption{Short caption with a verb in active voice.}
   \label{fig:slug}
   \end{figure}
   ```
