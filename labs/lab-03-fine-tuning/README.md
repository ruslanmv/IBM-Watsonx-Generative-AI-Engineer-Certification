# Lab 03 — Fine-tuning: datasets, LoRA, and InstructLab

> Exam alignment: **Section 3 — Fine-Tuning (31% — the biggest section)** · see `book/chapters/ch03-fine-tuning.tex`.

This lab covers the three watsonx fine-tuning ladders the exam tests:

1. **Prompt tuning** (soft prompt vectors) — cheapest, smallest artefact.
2. **LoRA / QLoRA** (adapter matrices, optionally on a 4-bit base) — the sweet spot for cost vs. quality.
3. **InstructLab** (taxonomy + synthetic data + multi-phase tuning) — when you need new knowledge *and* new skills at scale.

## What you will build

1. A clean JSONL dataset with train / validation / test splits.
2. A LoRA fine-tuning job launched via the **watsonx Tuning Studio API** on `ibm/granite-3-2-8b-instruct`.
3. A held-out evaluation that compares the tuned adapter to the few-shot baseline.
4. An **InstructLab taxonomy** leaf you could contribute upstream.

## Prerequisites

- Same watsonx credentials as labs 01 / 02.
- Tuning is a paid feature — expect modest GPU minutes per run on the smallest profile. The dataset in `dataset-prep/` is small (3,000 rows) and trains in roughly 30 minutes on the default tier.
- For InstructLab locally: `pipx install instructlab` (optional, not required to pass the exam).

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env       # edit credentials
```

## Run

```bash
python 01_dataset_prep.py                # build train/val/test JSONL
python 02_lora_tuning.py                 # launch LoRA tune (Tuning Studio)
python 03_evaluate_tuned_model.py        # F1 vs few-shot baseline
```

The InstructLab taxonomy sample is for review:

- `instructlab_taxonomy_sample.yaml` — a knowledge leaf you could `ilab data generate` from.

## Exam-relevant takeaways

- **Hard vs soft prompts**: hard = readable text, soft = learned float vectors.
- **LoRA** = freeze base, train rank-`r` matrices `A`, `B`. Effective update is `(α / r) · B · A`. Typical `r ∈ {4,8,16,32}`, `α = 2 · r`.
- **QLoRA** = LoRA on a 4-bit NF4-quantised base. Fits a 13B model on a single 24 GB GPU.
- **Quantisation ladder**: FP32 → FP16 / BF16 → INT8 (GPTQ, AWQ) → INT4 (NF4 / QLoRA).
- **InstructLab**: taxonomy tree (knowledge + skills) → synthetic data generation (LAB method) → multi-phase tuning.
- **Synthetic Data Generator** validates distribution fit with **Kolmogorov–Smirnov** (overall) and **Anderson–Darling** (tails), and protects privacy with budget ε, leakage δ, and a random seed.

## Files

| File | What it does |
|---|---|
| `01_dataset_prep.py` | Read raw labelled data, dedupe, balance, split, write JSONL |
| `02_lora_tuning.py` | Launch a LoRA tune via `TuneExperiment` |
| `03_evaluate_tuned_model.py` | Compare tuned adapter vs few-shot baseline on the test set |
| `instructlab_taxonomy_sample.yaml` | Sample knowledge leaf with seed examples |
| `dataset-prep/raw_tickets.csv` | Small synthetic seed CSV |
| `.env.example`, `requirements.txt` | Setup |

## Next

Proceed to [`labs/lab-04-rag`](../lab-04-rag) for production RAG.
