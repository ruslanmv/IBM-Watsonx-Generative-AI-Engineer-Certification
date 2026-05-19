import json, html, re, sys, glob, os

# Pick up the first C1000-185 question-bank JSON next to this script,
# or accept an explicit path as argv[1]. The bank is intentionally not
# committed — drop a fresh `C1000185vN.json` here when IBM publishes one.
HERE = os.path.dirname(os.path.abspath(__file__))
if len(sys.argv) > 1:
    bank_path = sys.argv[1]
else:
    candidates = sorted(glob.glob(os.path.join(HERE, 'C1000185*.json'))) \
              or sorted(glob.glob(os.path.join(HERE, '*c1000-185*.json'))) \
              or sorted(glob.glob(os.path.join(HERE, '*.json')))
    if not candidates:
        sys.exit('No question-bank JSON found in docs/quizzes/. Pass a path as argv[1].')
    bank_path = candidates[-1]

with open(bank_path) as f:
    qs = json.load(f)

def topic(q):
    t = (q['question'] + ' ' + ' '.join(q['options'])).lower()
    s = {}
    s['rag'] = sum(t.count(k) for k in ['rag', 'retrieval', 'vector', 'embedding', 'faiss', 'chroma', 'langchain', 'chunk'])
    s['finetune'] = sum(t.count(k) for k in ['fine-tun', 'fine tun', 'lora', 'qlora', 'peft', 'instructlab', 'quantiz', 'synthetic data', 'taxonom', 'soft prompt'])
    s['prompt'] = sum(t.count(k) for k in ['prompt', 'temperature', 'top-k', 'top-p', 'top_k', 'top_p', 'few-shot', 'zero-shot', 'chain-of-thought', ' cot ', 'token', 'penalt', 'beam search', 'greedy'])
    s['deploy'] = sum(t.count(k) for k in ['deploy', 'production', 'monitor', 'latency', 'scale', 'api endpoint', 'sdk', 'gateway', 'cloud pak'])
    s['gov'] = sum(t.count(k) for k in ['governance', 'bias', 'fairness', 'guardian', 'hap ', 'pii', 'jailbreak', 'ethic', 'compliance', 'factsheet', 'guardrail'])
    s['integration'] = sum(t.count(k) for k in ['agent', 'mcp', 'watson assistant', 'discovery', 'orchestrat', 'workflow'])
    s['fundamentals'] = sum(t.count(k) for k in ['hallucinat', 'context window', 'capabilit', 'limitation', 'transformer', 'foundation model'])
    s['setup'] = sum(t.count(k) for k in ['watsonx.ai', 'project', 'space', 'cloud account'])
    cat = max(s.items(), key=lambda x: x[1])
    return cat[0] if cat[1] > 0 else 'general'

by_cat = {}
for i, q in enumerate(qs):
    by_cat.setdefault(topic(q), []).append(i)

def is_simple(q):
    return len(q['options']) <= 5 and len(q.get('correct_labels', [])) == 1

PLANS = {
    'youtube': {
        'm1': ['setup', 'fundamentals', 'gov', 'general', 'setup'],
        'm2': ['fundamentals', 'prompt', 'prompt', 'general', 'rag'],
        'm3': ['prompt'] * 5,
        'm4': ['finetune'] * 5,
        'm5': ['rag'] * 5,
        'm6': ['deploy'] * 5,
        'm7': ['integration', 'gov', 'prompt', 'finetune', 'deploy'],
    },
    'udemy': {
        's1': ['setup', 'fundamentals', 'gov', 'general', 'fundamentals'],
        's2': ['fundamentals', 'prompt', 'prompt', 'rag', 'general'],
        's3': ['prompt'] * 5,
        's4': ['finetune'] * 5,
        's5': ['rag'] * 5,
        's6': ['deploy'] * 5,
        's7': ['integration', 'integration', 'deploy', 'prompt', 'rag'],
        's8': ['gov'] * 5,
        's9': ['prompt', 'finetune', 'rag', 'deploy', 'gov'],
    },
}

def pick(cat, used, fallback_order=('prompt','finetune','rag','deploy','gov','integration','fundamentals','setup','general')):
    pools = [cat] + [c for c in fallback_order if c != cat]
    for c in pools:
        candidates = [i for i in by_cat.get(c, []) if i not in used and is_simple(qs[i])]
        if candidates:
            choice = candidates[0]
            used.add(choice)
            return choice
    for i in range(len(qs)):
        if i not in used:
            used.add(i)
            return i

labels = {
    'm1': ('Module 1 Quiz', '01 / Getting Started'),
    'm2': ('Module 2 Quiz', '02 / Fundamentals'),
    'm3': ('Module 3 Quiz', '03 / Prompt Engineering'),
    'm4': ('Module 4 Quiz', '04 / Fine-Tuning'),
    'm5': ('Module 5 Quiz', '05 / RAG'),
    'm6': ('Module 6 Quiz', '06 / Deployment'),
    'm7': ('Module 7 Quiz', '07 / Exam Strategy'),
    's1': ('Section 1 Quiz', 'S1 / Intro & Setup'),
    's2': ('Section 2 Quiz', 'S2 / Fundamentals'),
    's3': ('Section 3 Quiz', 'S3 / Prompt Engineering'),
    's4': ('Section 4 Quiz', 'S4 / Fine-Tuning'),
    's5': ('Section 5 Quiz', 'S5 / RAG'),
    's6': ('Section 6 Quiz', 'S6 / Deployment'),
    's7': ('Section 7 Quiz', 'S7 / Integration'),
    's8': ('Section 8 Quiz', 'S8 / Governance'),
    's9': ('Section 9 Quiz', 'S9 / Exam Prep'),
}

def render_quiz_flat(key, footer_prefix, question_ids):
    """Render 5 flat <section> blocks suitable for inserting inside an existing vertical stack."""
    lbl, foot_suffix = labels[key]
    footer = f'{footer_prefix} · {foot_suffix}'
    out = []
    for n, qid in enumerate(question_ids, 1):
        q = qs[qid]
        qtext = html.escape(q['question'])
        out.append(f'<section>')
        out.append(f'  <span class="checkpoint-label">✅ {lbl} · Q{n} / 5</span>')
        out.append(f'  <p class="checkpoint-q">{qtext}</p>')
        out.append(f'  <ul class="checkpoint-opts">')
        correct_labels = set(q.get('correct_labels', []))
        for opt in q['options']:
            m = re.match(r'^\s*([A-Z])\.\s*(.*)', opt)
            if m:
                letter, rest = m.group(1), m.group(2)
                cls = ' class="correct"' if letter in correct_labels else ''
                out.append(f'    <li{cls}><strong>{letter}.</strong> {html.escape(rest)}</li>')
            else:
                out.append(f'    <li>{html.escape(opt)}</li>')
        out.append(f'  </ul>')
        correct_str = ', '.join(sorted(correct_labels)) if correct_labels else '—'
        out.append(f'  <p class="xsmall" style="margin-top:10px; text-align:left;"><span class="hl3">Answer: {correct_str}</span> &nbsp;·&nbsp; the correct option is highlighted in green. Real-style C1000-185 question.</p>')
        out.append(f'  <aside class="slide-footer">{footer} · Q{n}</aside>')
        out.append(f'</section>')
    return '\n'.join(out)

rendered = {'youtube': {}, 'udemy': {}}
for deck, plan in PLANS.items():
    used = set()
    footer_prefix = 'ruslanmv.com · C1000-185'
    for key, cats_list in plan.items():
        ids = [pick(c, used) for c in cats_list]
        rendered[deck][key] = render_quiz_flat(key, footer_prefix, ids)

with open('/tmp/quizzes.json', 'w') as f:
    json.dump(rendered, f)

print('done. Keys:', list(rendered['youtube'].keys()), '+', list(rendered['udemy'].keys()))
