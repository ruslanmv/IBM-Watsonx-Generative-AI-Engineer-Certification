# Lab 02 — Prompt engineering: zero / few-shot, parameters, templates

> Exam alignment: **Section 2 — Prompt Engineering (16%)** · see `book/chapters/ch02-prompt-engineering.tex`.

In this lab you compare zero-shot, few-shot, and chain-of-thought prompting; sweep the model parameters; store a versioned **prompt template** in your watsonx project; and screen inputs with **Granite Guardian**.

## What you will build

1. A zero/few-shot/CoT bake-off on the same classification task.
2. A parameter sweep (`temperature`, `top_p`, `repetition_penalty`) with a tiny rubric.
3. A **versioned prompt template** stored in your project via `PromptTemplateManager`.
4. A Granite Guardian wrap around the model call.

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # edit credentials
```

## Run

```bash
python 01_zero_few_shot.py          # compare prompting styles
python 02_parameter_sweep.py        # temperature × top_p × decoding
python 03_prompt_template.py        # store + recall a versioned template
python 04_guardian_check.py         # input + output safety filter
```

## Exam-relevant takeaways

- **Few-shot** = 2–5 examples in the prompt. It anchors format and vocabulary, but each example costs tokens.
- **Chain-of-thought** = ask the model to reason step-by-step; unlocks math and logic.
- **Greedy decoding** is deterministic. **Sampling** + `top_p` / `top_k` + `random_seed` is creative *and* reproducible.
- A **prompt template** is the production unit: a versioned, named asset with input variables and a pinned model.
- Wrap public endpoints with **Granite Guardian** for HAP / PII / jailbreak / groundedness checks.

## Files

| File | What it does |
|---|---|
| `01_zero_few_shot.py` | Same task in three prompting styles |
| `02_parameter_sweep.py` | Grid over temperature × top_p × decoding |
| `03_prompt_template.py` | `PromptTemplateManager`: store, list, load, delete |
| `04_guardian_check.py` | Granite Guardian input + output filtering |
| `.env.example`, `requirements.txt` | Setup |

## Next

Proceed to [`labs/lab-03-fine-tuning`](../lab-03-fine-tuning) for LoRA + InstructLab.
