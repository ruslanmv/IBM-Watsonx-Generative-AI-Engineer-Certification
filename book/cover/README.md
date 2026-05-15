# Cover artwork for Amazon KDP

KDP requires **two separate cover files** depending on the format you sell:

| Format | Dimensions | Bleed | File type |
|---|---|---|---|
| **Kindle eBook** | 2,560 × 1,600 px minimum, 1.6:1 ratio (~2,560 × 1,600 is the safe sweet spot) | None | JPEG / TIFF, RGB, 72 dpi+ |
| **Paperback (6” × 9”)** | Full wrap: front + spine + back, with **0.125” bleed** on all four outside edges | Yes — 0.125” | PDF, CMYK, 300 dpi |

The paperback spine width depends on the page count of the printed PDF:

> **Spine width (white paper, in.)** = `page_count × 0.002252`

A 300-page study guide therefore needs **\~0.68 in** of spine.

KDP’s **Cover Calculator** generates a perfectly-sized template once you know the trim size and page count:

<https://kdp.amazon.com/cover-calculator>

## Recommended workflow

1. Generate the manuscript PDF with `./build.sh print` (from the parent directory).
2. Note the final page count from `main.pdf` (`pdfinfo main.pdf` or open it in any viewer).
3. Plug that page count into the KDP Cover Calculator to download a template.
4. Open the template in Affinity Publisher, Adobe InDesign, Canva (Pro), or Figma.
5. Save the front-only Kindle cover as JPEG; save the full wrap as PDF.
6. Place the final artwork in this directory:
   - `cover/kindle_cover.jpg`
   - `cover/paperback_wrap.pdf`

## Design notes that match the book / slide-deck branding

Keep the visual language consistent with the YouTube and Udemy editions so buyers recognise the series:

| Token | Value |
|---|---|
| Background | Near-black `#0A0E1A` |
| Primary accent | Indigo `#7C8AFF` |
| Secondary accent | Teal `#4ECDC4` |
| Heading font | Outfit (800 weight) |
| Mono font | JetBrains Mono |

Front-cover text block:

```
IBM watsonx
Generative AI Engineer — Associate
Exam C1000-185

Complete Study Guide & Exam Workbook

Ruslan Idelfonso Magana Vsevolodovna
```

Keep the IBM blue stripe small and inside the front cover — the book is independently produced; do not use the IBM logo on the cover.

## Submitting on KDP

* **Kindle eBook:** upload `kindle_cover.jpg` in the *Kindle eBook Cover* step.
* **Paperback:** upload `paperback_wrap.pdf` in the *Paperback Cover* step (skip the *Cover Creator* tool; the PDF wrap is more reliable).

KDP will re-render a preview — review it for the spine alignment and bleed before approving.
