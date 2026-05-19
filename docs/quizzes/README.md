# Quiz Source — C1000-185 End-of-Session Self-Tests

This folder holds the generator that produces the 5-question quizzes embedded
at the end of every module in the YouTube deck (`docs/index.html`) and every
section in the Udemy deck (`udemy/index.html`).

## Files

| File | Purpose |
|---|---|
| `build_quizzes.py` | Generator — picks 5 topic-aligned questions per module/section and renders Reveal.js `<section>` blocks |

> The question-bank JSON itself is **not committed** — drop a fresh
> `C1000185vN.json` next to `build_quizzes.py` (or update the path inside
> the script) and re-run. This keeps the bank independently updatable
> without churning git history.

## How the quizzes are designed

**Goal:** when a learner finishes a video / lecture, they should be able to answer
five exam-style questions without leaving the slide deck.

1. Each question in the bank is auto-classified by topic (prompt, fine-tune, RAG,
   deploy, governance, integration, fundamentals, setup) via keyword scoring.
2. A per-deck plan maps each module / section to a sequence of topics.
3. The generator picks the first un-used, single-answer, ≤5-option question per
   slot and renders it as a Reveal.js `<section>` with the correct option marked
   `class="correct"` (highlighted in green by the existing slide CSS).
4. The output of the generator is patched into `docs/index.html` and
   `udemy/index.html` in place of the original single-question checkpoints.

## Re-running the generator

```bash
cd docs/quizzes
python3 build_quizzes.py
# Then re-run the injection script if you change the plan — see
# the commit message that introduced the quizzes for the inject script.
```

## Distribution

| Deck | Modules / sections | Total quiz questions |
|---|---|---|
| YouTube (`docs/index.html`) | 7 modules × 5 | 35 |
| Udemy (`udemy/index.html`) | 9 sections × 5 | 45 |

Every question is single-answer (A/B/C/D), four options, with the correct option
highlighted on the same slide plus a one-line rationale.
