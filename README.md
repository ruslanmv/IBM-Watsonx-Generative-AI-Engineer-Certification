<div align="center">

# IBM watsonx Generative AI Engineer — Associate
### Complete Certification Course · Exam **C1000-185**

> The open, multi-format, exam-aligned course for the IBM watsonx Generative AI Engineer Associate certification — slide decks, hands-on labs, mock exams, and a LaTeX study guide. Built for self-learners and study groups.

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](./LICENSE)
[![Exam Aligned: C1000-185](https://img.shields.io/badge/Exam-C1000--185-0F62FE?logo=ibm&logoColor=white)](https://www.ibm.com/training/certification/C1000-185)
[![Slides: live](https://img.shields.io/badge/Slides-Live%20on%20GitHub%20Pages-7c8aff)](https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/)
[![Format: LaTeX Book](https://img.shields.io/badge/Book-LaTeX-008080)](./book)
[![YouTube](https://img.shields.io/badge/YouTube-Tutorials-FF0000?logo=youtube&logoColor=white)](./docs)
[![Udemy](https://img.shields.io/badge/Udemy-Course-A435F0?logo=udemy&logoColor=white)](./udemy)
[![Stars](https://img.shields.io/github/stars/ruslanmv/IBM-Watsonx-Generative-AI-Engineer-Certification?style=social)](https://github.com/ruslanmv/IBM-Watsonx-Generative-AI-Engineer-Certification/stargazers)

<br>

**Instructor: [Ruslan Idelfonso Magana Vsevolodovna](https://ruslanmv.com)** — Senior AI engineer · IBM watsonx practitioner
<sub>Same instructor, same series as **Agentic AI from Scratch** and the **watsonx Workshop**.</sub>

[📺 Open the YouTube deck](https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/docs/) ·
[🎓 Open the Udemy deck](https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/udemy/) ·
[📘 Official exam guide](./docs/official/guide.pdf) ·
[🧪 Hands-on labs](./labs) ·
[⭐ Star this repo](https://github.com/ruslanmv/IBM-Watsonx-Generative-AI-Engineer-Certification)

</div>

---

## 🎯 The exam in 4 numbers

<div align="center">

| Questions | To pass | Time | Sections |
|:---------:|:-------:|:----:|:--------:|
| **62**    | **44** (71%) | **90 min** | **6** |

</div>

You have **~87 seconds per question** — pacing matters more than recall. This course is engineered around the official C1000-185 blueprint, with study-time allocation proportional to each section's weight.

---

## 💡 What you will learn

By the end of this course you will be able to:

- 🧠 **Design** a generative AI solution end-to-end on watsonx.ai — picking between prompting, RAG, fine-tuning and agents using a single decision tree.
- ✍️ **Engineer** prompts the production way — versioned prompt templates, parameter tuning (greedy/sampling, temperature, top-k, top-p, stop sequences), CRISPE/APE/CARE frameworks.
- 🔧 **Customise models** with PEFT — LoRA, QLoRA, prompt tuning, and IBM **InstructLab** (taxonomy + synthetic data generation + LAB methodology).
- 📚 **Build production RAG** — embeddings (Slate v2, Granite Embedding multilingual), vector stores (FAISS, Chroma, watsonx Discovery), hybrid search, re-ranking, agentic RAG and AutoRAG.
- 🚀 **Deploy** — Deployment Spaces, prompt template promotion, custom-model serving, **Model Gateway**, watsonx **AI Pipelines** for corpus refresh, SaaS vs. Cloud Pak for Data.
- 🔗 **Integrate** — Watson Assistant, Watson Discovery, watsonx.governance, **Model Context Protocol (MCP)**, LangChain tool-calling agents.
- 🛡️ **Secure & govern** with **Granite Guardian** (HAP / PII / jailbreaks / groundedness) and watsonx.governance factsheets.
- 🎓 **Pass C1000-185 on the first try** with three full mock exams and a 30-day study plan.

> **All code uses the current 2026 model catalogue:** `ibm/granite-3-2-8b-instruct`, `meta-llama/llama-3-3-70b-instruct`, `mistralai/mistral-large`, `ibm/granite-embedding-278m-multilingual`, `ibm/slate-125m-english-rtrvr-v2`, `ibm/granite-guardian-3-8b`, and the `ibm-watsonx-ai` Python SDK. **Deprecated identifiers** (`granite-13b-*`, `llama-2-*`, `flan-t5-*`, `mpt-*`) are flagged so you recognise them on the exam but never pick them in new work.

---

## 📚 Pick your format

<table>
<tr>
<td width="33%" valign="top">

### 📺 YouTube edition
**Free · 7 modules · 26 lessons · ~5 hours**

A focused, no-fluff cert-prep track. Watch on YouTube or use the slide deck to revise.

→ [`docs/`](./docs) — Reveal.js slide deck
→ [`docs/scripts/`](./docs/scripts) — Video scripts
→ [Live deck](https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/docs/)

</td>
<td width="33%" valign="top">

### 🎓 Udemy edition
**Extended · 10 sections · 40+ hours**

Deep-dive lectures, quizzes per section, lab callouts, **three full mock exams**, graded assignments.

→ [`udemy/`](./udemy) — Lectures + labs + resources
→ [Course outline](./udemy/README.md)
→ [Live deck](https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/udemy/)

</td>
<td width="33%" valign="top">

### 📘 Study book (LaTeX)
**Self-study · 8 chapters · 40-question mock**

Publication-ready PDF for Kindle / print. Maps 1:1 to the exam blueprint.

→ [`book/`](./book) — LaTeX source
→ Build: `cd book && ./build.sh`
→ [TOC](./book/main.tex)

</td>
</tr>
</table>

You do not need to pick one. Most students watch the YouTube series first, then drill the Udemy quizzes and mock exams, then revise from the LaTeX book and cheat sheet the night before the exam.

---

## 🗺️ Course content

The Udemy edition has the most depth. The YouTube edition compresses it into the cert-prep essentials. Both follow the **official C1000-185 blueprint**.

<details open>
<summary><b>Section 1 — Course Intro &amp; watsonx Setup · 2 h</b></summary>

- 1.1 Welcome &amp; Roadmap
- 1.2 Exam Overview and Certification Path
- 1.3 Setting up your watsonx.ai environment
- 1.4 Platform navigation tour
- 1.5 Study strategy for success
- **Lab 1.1** Create your IBM Cloud account · **Lab 1.2** First prompt in Prompt Lab

</details>

<details>
<summary><b>Section 2 — Generative AI Fundamentals · 8 h · <i>15% of exam</i></b></summary>

- The five capabilities: Summarization, Classification, Generation (Code, Translation), Extraction, Q&amp;A
- GenAI patterns: Transformer, **MoE**, VAE, Reasoning models
- Knowledge cutoff, hallucination, bias, context window
- The watsonx.ai model catalogue (Granite, Llama, Mistral, Guardian, Embedding)
- Architecture decision tree: prompting / RAG / fine-tuning / agents
- **Labs 2.1–2.3** · **Assignment 1** Capability matching

</details>

<details>
<summary><b>Section 3 — Prompt Engineering Mastery · 12 h · <i>16% of exam</i></b></summary>

- Zero-shot, few-shot, chain-of-thought, self-consistency, least-to-most
- CRISPE · APE · CARE frameworks
- Prompt parameters in depth: temperature, top-k, top-p, random seed, repetition penalty, min/max tokens, stop sequences, time limit
- Prompt Lab modes: Chat · Structured · Freeform
- Prompt templates, variables, versioning
- Prompt risks: injection, leaking, jailbreaks, PII filter, HAP filter
- **Labs 3.1–3.5** · **Assignments 3 &amp; 4**

</details>

<details>
<summary><b>Section 4 — Fine-Tuning &amp; Customization · 16 h · <i>★ 31% of exam (largest)</i></b></summary>

- Hard vs **soft prompts**, prompt tuning
- **PEFT / LoRA / QLoRA** — math, hyperparameters, target modules
- Quantization: FP16 → INT8 → INT4, PTQ, QAT, GPTQ, AWQ, NF4
- Dataset prep, splits, JSONL, **Data Refinery**
- **InstructLab**: taxonomy, synthetic data generation, **LAB methodology**, multi-phase tuning
- Synthetic Data UI: existing-data vs schema mode; **Kolmogorov–Smirnov** + **Anderson–Darling**; differential privacy (ε, δ, random seed)
- watsonx Tuning Studio walkthrough
- Hyperparameter selection · evaluation · cost optimization
- **Labs 4.1–4.6** · **Assignments 5 &amp; 6**

</details>

<details>
<summary><b>Section 5 — Retrieval-Augmented Generation (RAG) · 14 h · <i>17% of exam</i></b></summary>

- Embeddings (Slate v2, Granite Embedding multilingual, third-party)
- Vector stores (FAISS, Chroma, Milvus, pgvector, Elasticsearch dense_vector, SingleStore)
- Retrievers: embedded vs static, Watson Discovery (legacy), GitHub Code Retrieval API, **watsonx Discovery**
- Chunking strategies, hybrid search, re-ranking
- LangChain + watsonx, LangChain + Watson ML + Elasticsearch, LangChain + SingleStore, LlamaIndex
- **Agentic RAG** and **AutoRAG**
- **Labs 5.1–5.7** · **Assignments 7 &amp; 8**

</details>

<details>
<summary><b>Section 6 — Deployment &amp; Production · 8 h · <i>13% of exam</i></b></summary>

- Project → Space (Dev/Staging/Prod) → REST endpoint
- Deploying prompt templates, tuned models, AI services
- API + SDK · authentication · versioning · A/B testing
- High availability and scalability · cost optimization
- **Model Gateway** · SaaS vs Cloud Pak for Data (Software)
- Corpus management via **watsonx AI Pipelines**
- **Labs 6.1–6.5** · **Assignment 9**

</details>

<details>
<summary><b>Section 7 — Integration &amp; Orchestration · 6 h · <i>8% of exam</i></b></summary>

- watsonx.ai REST API and Python SDK
- Watson Assistant + watsonx integration
- LangChain agents, chains, tools, memory
- Multi-model and event-driven architectures
- **Model Context Protocol (MCP)** for vendor-neutral tool integration
- **Labs 7.1–7.4** · **Assignment 10**

</details>

<details>
<summary><b>Section 8 — Governance, Ethics &amp; Best Practices · 4 h</b></summary>

- AI governance frameworks: NIST AI RMF · EU AI Act · ISO 42001 · GDPR
- Bias detection and mitigation
- **Granite Guardian** categories: HAP, PII, jailbreak, bias, groundedness
- Model cards / factsheets in watsonx.governance
- Compliance and audit-ready evidence

</details>

<details>
<summary><b>Section 9 — Exam Preparation · 8 h</b></summary>

- Exam structure, pacing, question patterns
- Scenario walkthroughs
- **3 full 62-question mock exams** with explanations
- Topic-specific quick quizzes
- Last-minute review topics &amp; exam-day checklist

</details>

<details>
<summary><b>Section 10 — Bonus: Advanced Topics · optional</b></summary>

- Multi-modal foundation models (image + text)
- Advanced agent architectures (LangGraph state machines, CrewAI)
- Custom tool development with MCP
- Performance optimisation techniques
- Future trends in GenAI

</details>

---

## 🧪 Hands-on labs

| # | Lab | Topic | Watsonx feature |
|---|---|---|---|
| 1 | First Prompt | Prompt Lab basics | Prompt Lab · Granite 3.x |
| 2 | Few-Shot in Action | Anchor format and vocabulary | Prompt templates |
| 3 | Parameter Tuning | Sweep temperature / top-p | Prompt Lab parameters |
| 4 | LoRA Fine-Tune | Train a classifier in 30 min | Tuning Studio · QLoRA |
| 5 | InstructLab Customisation | Knowledge + skills tuning | InstructLab · LAB method |
| 6 | Synthetic Data Generation | Existing-data + schema modes | Synthetic Data Generator |
| 7 | Basic RAG | Slate + FAISS in a notebook | Embeddings API |
| 8 | Production RAG | Hybrid search + re-ranking | watsonx Discovery |
| 9 | Deployment | Online + batch endpoints | Deployment Spaces · Model Gateway |
| 10 | End-to-End Integration | LangChain agent with MCP tools | ChatWatsonx + AgentExecutor |

Each lab ships a **starter** notebook, a **solution** notebook, and a metrics rubric.

---

## 🏆 Three full mock exams

| Mock | Style | Pass target | What it tests |
|------|-------|------------|---------------|
| **Mock 1** | Foundation, balanced | ≥ 60% | Recall across all 6 sections |
| **Mock 2** | Scenario-heavy | ≥ 70% | Fine-tuning &amp; RAG deep dives |
| **Mock 3** | Exam simulation | ≥ 75% | Full 62 Qs in 90 min — book the exam after this |

Every wrong answer ships with a 100-word explanation and a pointer back to the exact chapter / lecture.

---

## 👤 Who this course is for

- 🧑‍💻 **AI / ML engineers** validating their watsonx skills with a recognised credential
- 📊 **Data scientists** moving into generative AI implementation
- 🧭 **Solution architects** designing AI-powered enterprise solutions on IBM Cloud
- 🎓 **Self-learners** who want a structured, exam-aligned path
- 🏢 **Teams** doing a watsonx pilot and needing one curriculum across roles

---

## 📋 Prerequisites

| Required | Recommended |
|----------|-------------|
| Python 3.10+ (basics) | 6–12 months hands-on ML/AI |
| IBM Cloud account (free tier) | Familiarity with REST APIs |
| Reading English-language technical docs | Comfort with Jupyter notebooks |
| 4–12 weeks of study time | Linux command line basics |

**For the book:** TeX Live or MiKTeX (or build in [Overleaf](https://overleaf.com)).
**For the labs:** Python 3.10+, `pip install ibm-watsonx-ai langchain-ibm faiss-cpu`.

---

## 🗓️ 30-day study plan

| Week | Focus | Hours |
|------|-------|-------|
| **1** | Foundations + Prompt Engineering (Ch. 1–2) | 8 |
| **2** | Fine-Tuning deep dive (Ch. 3 — biggest section) | 10 |
| **3** | RAG + Deployment + Integration (Ch. 4–6) | 8 |
| **4** | Mock exams, weak-area review, cheat sheet | 6 |
| | **Total** | **~32 h** |

Best practitioners finish in 4 weeks. Beginners: budget 12 weeks at the same daily cadence.

---

## 📂 Repository structure

```
ibm-c1000-185-certification/
├── book/                         📘 LaTeX study guide (8 chapters + 4 appendices)
│   ├── main.tex                  ·   Main document
│   ├── chapters/                 ·   ch01-foundations … ch06-integration
│   │                                 + frontmatter, glossary, mock exam, answer key, cheat sheet
│   └── build.sh                  ·   `./build.sh` to produce main.pdf
│
├── docs/                         📺 YouTube edition
│   ├── index.html                ·   Reveal.js slide deck (live on GitHub Pages)
│   ├── slides/                   ·   Per-video slide HTMLs
│   ├── scripts/                  ·   Video narration scripts (markdown)
│   └── official/guide.pdf        ·   The official IBM C1000-185 study guide
│
├── udemy/                        🎓 Udemy edition
│   ├── index.html                ·   Extended Reveal.js slide deck
│   ├── lectures/                 ·   10 sections, 40+ hours of detailed content
│   ├── labs/                     ·   Step-by-step lab walkthroughs
│   ├── assignments/              ·   10 graded assignments
│   └── resources/                ·   Cheat sheets, templates, practice exams
│
├── labs/                         🧪 Quick hands-on labs (notebook-first)
│   ├── lab-01-foundations/
│   ├── lab-02-prompt-engineering/
│   ├── lab-03-fine-tuning/
│   ├── lab-04-rag/
│   ├── lab-05-deployment/
│   └── lab-06-integration/
│
├── index.html                    🌐 Course landing page (deployed via GH Pages)
└── .github/
    └── workflows/
        └── deploy-pages.yml      🚀 CI: publishes docs + udemy + landing to GitHub Pages
```

---

## 🚀 Quick start

### 1. Browse the live course site

After enabling GitHub Pages (Settings → Pages → Source: **GitHub Actions**), the course is reachable at:

🔗 **<https://ruslanmv.github.io/IBM-Watsonx-Generative-AI-Engineer-Certification/>**

### 2. Build the LaTeX book

```bash
cd book
./build.sh                # produces main.pdf
# or, manually:
pdflatex main.tex && bibtex main && pdflatex main.tex && pdflatex main.tex
```

### 3. Open the slide decks locally

```bash
# YouTube deck
open docs/index.html              # macOS
xdg-open docs/index.html          # Linux

# Udemy deck
open udemy/index.html
```

The decks are pure HTML — no build step. Press <kbd>?</kbd> in the deck for keyboard shortcuts (use <kbd>S</kbd> for the speaker-notes view when recording).

### 4. Run a hands-on lab

```bash
pip install ibm-watsonx-ai langchain-ibm faiss-cpu jupyter
export WATSONX_APIKEY=<your-api-key>
export WATSONX_PROJECT_ID=<your-project-id>
jupyter lab labs/lab-04-rag/exercises.ipynb
```

---

## 👤 Your instructor

<table>
<tr>
<td width="160" valign="top" align="center">

<a href="https://ruslanmv.com">
  <img src="https://github.com/ruslanmv.png" width="120" alt="Ruslan Idelfonso Magana Vsevolodovna">
</a>

</td>
<td valign="top">

### Ruslan Idelfonso Magana Vsevolodovna
**Senior AI engineer · IBM watsonx practitioner · author at [ruslanmv.com](https://ruslanmv.com)**

I build production AI for enterprises and teach what I learn on YouTube and Udemy. This course is part of a series with **[Agentic AI from Scratch](https://github.com/ruslanmv/agentic-ai-tutorial)** (LangChain · LangGraph · CrewAI) and the **[watsonx Workshop](https://github.com/ruslanmv/watsonx-workshop)** (end-to-end RAG application).

> *"Build it on the platform, prove it with metrics, then explain it like a teacher."*

🌐 [ruslanmv.com](https://ruslanmv.com) · 💼 [LinkedIn](https://www.linkedin.com/in/ruslanmv/) · 🐙 [@ruslanmv](https://github.com/ruslanmv)

</td>
</tr>
</table>

---

## ❓ FAQ

<details>
<summary><b>Do I need prior AI experience?</b></summary>

Basic Python and a curiosity about machine learning are enough. Sections 1–2 cover the GenAI fundamentals from scratch.
</details>

<details>
<summary><b>Is this an official IBM course?</b></summary>

No. This is an **independent, community-built** course aligned to the publicly-published C1000-185 exam blueprint. IBM, watsonx, watsonx.ai, watsonx.governance, watsonx.data, Granite and InstructLab are trademarks of IBM Corporation. The official IBM exam guide is bundled in `docs/official/guide.pdf` for reference.
</details>

<details>
<summary><b>How long will it take me to prepare for C1000-185?</b></summary>

- **Practitioners** with prior LLM experience: **~4 weeks** at 8 h/week.
- **Intermediate** ML engineers: **~8 weeks** at 6 h/week.
- **Beginners**: **~12 weeks** at 6 h/week.

Allocate study time **proportional to section weights** — fine-tuning is 31% of the exam, so it deserves 31% of your prep.
</details>

<details>
<summary><b>Will the materials stay updated as watsonx evolves?</b></summary>

Yes. Code samples and model IDs are pinned to the **current 2026 watsonx.ai catalogue** (Granite 3.x, Llama 3.3, Mistral, Granite Guardian, Granite Embedding, Slate v2). Deprecated identifiers (`granite-13b-*`, `llama-2-*`, `flan-t5-*`, `mpt-*`) are explicitly flagged as legacy.
</details>

<details>
<summary><b>What if I fail the exam?</b></summary>

IBM's policy is a 24-hour cooldown before retaking. Use the answer-key explanations in Appendix C to identify weak chapters, revise from the cheat sheet (Appendix D), and retake. Most students who fail the first time pass within a week.
</details>

<details>
<summary><b>Can I use this for an internal corporate training programme?</b></summary>

Yes — the repository is **Apache 2.0 licensed**. You can fork it, adapt the LaTeX book, host the slides on your intranet, and use the labs in workshops. Attribution is appreciated. The Apache 2.0 license also grants an explicit patent licence — useful for enterprise legal review.
</details>

<details>
<summary><b>How do I report an error or contribute?</b></summary>

Open an issue or a pull request. See <a href="#-contributing">Contributing</a> below.
</details>

---

## 🤝 Contributing

Contributions, corrections, and translations are welcome.

1. **Issues** — typos, broken links, outdated model IDs, exam scope changes.
2. **PRs** — please match the existing chapter / slide structure and the design system (dark theme `#0a0e1a` / accent `#7c8aff` / Outfit + JetBrains Mono).
3. **LaTeX** — ensure `cd book && ./build.sh` runs cleanly before opening a PR.
4. **Code** — pin to current 2026 model IDs and the `ibm-watsonx-ai` SDK.

For bigger contributions (a new lab, a whole appendix), please open an issue first to align scope.

By contributing, you agree that your contribution is licensed under the Apache License 2.0.

---

## 🔗 Official IBM resources

- [**Exam C1000-185 page**](https://www.ibm.com/training/certification/C1000-185)
- [**Official study guide (PDF)**](./docs/official/guide.pdf) — bundled here for reference
- [**watsonx.ai documentation**](https://www.ibm.com/docs/en/watsonx)
- [**watsonx.ai API reference**](https://cloud.ibm.com/apidocs/watsonx-ai)
- [**InstructLab on GitHub**](https://github.com/instructlab)
- [**Granite models on Hugging Face**](https://huggingface.co/ibm-granite)
- [**Pearson VUE (exam scheduling)**](https://home.pearsonvue.com/ibm)

---

## 🌐 Companion courses by the same instructor

| Repo | What it covers |
|------|----------------|
| [**ruslanmv/agentic-ai-tutorial**](https://github.com/ruslanmv/agentic-ai-tutorial) | Build production agents in LangChain, LangGraph, and CrewAI — one problem, three frameworks |
| [**ruslanmv/watsonx-workshop**](https://github.com/ruslanmv/watsonx-workshop) | End-to-end RAG application on watsonx + accelerator notebooks |
| [**ruslanmv/ai-tutorial-generator**](https://github.com/ruslanmv/ai-tutorial-generator) | The toolchain that produces these courses |

---

## 📝 License

This project is licensed under the **Apache License 2.0** — see [LICENSE](./LICENSE) for the full terms.

> IBM, watsonx, watsonx.ai, watsonx.data, watsonx.governance, Granite, and InstructLab are trademarks or registered trademarks of IBM Corporation. This study guide is an independent, community publication and is not authorised, sponsored, or otherwise approved by IBM Corporation.

---

<div align="center">

### ⭐ If this course helps you pass the exam, please star the repository.

Word of mouth is how this series grows.
Found a bug or have feedback? [Open an issue](https://github.com/ruslanmv/IBM-Watsonx-Generative-AI-Engineer-Certification/issues/new) — I read every one.

Made with care by **Ruslan Idelfonso Magana Vsevolodovna** · [ruslanmv.com](https://ruslanmv.com) · 2026

</div>
