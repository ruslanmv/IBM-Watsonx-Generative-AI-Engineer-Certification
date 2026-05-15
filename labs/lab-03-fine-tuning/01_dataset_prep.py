"""
Lab 03 · step 1 — Dataset preparation for fine-tuning.

Given a small CSV of labelled support tickets, we:
  1. Drop exact + near-duplicates.
  2. Balance class frequencies (down-sample dominant classes).
  3. Stratified split into train / val / test (70 / 15 / 15).
  4. Write JSONL files in the format watsonx Tuning Studio expects.

Run:
    python 01_dataset_prep.py

Exam note: never evaluate on training data. Always keep a clean test split.
"""
import json
import os
from pathlib import Path
from dotenv import load_dotenv
import pandas as pd
from sklearn.model_selection import train_test_split

load_dotenv()
DATA_DIR = Path(os.getenv("DATA_DIR", "./dataset-prep"))
DATA_DIR.mkdir(parents=True, exist_ok=True)
raw_path = DATA_DIR / "raw_tickets.csv"

# Bootstrap a tiny seed CSV the first time you run this.
if not raw_path.exists():
    seed = [
        ("my charge is wrong",            "BILLING"),
        ("refund my last invoice please", "BILLING"),
        ("the app keeps crashing",        "TECH"),
        ("setup wizard freezes",          "TECH"),
        ("i cannot reset my password",    "TECH"),
        ("can I cancel my account?",      "OTHER"),
        ("do you have a French version?", "OTHER"),
        ("my charge is wrong",            "BILLING"),       # dup
    ]
    pd.DataFrame(seed, columns=["text", "label"]).to_csv(raw_path, index=False)
    print(f"Wrote a tiny seed CSV at {raw_path}")

df = pd.read_csv(raw_path)
print(f"Loaded {len(df)} rows; class counts:\n{df['label'].value_counts()}")

# 1) De-duplicate
df = df.drop_duplicates(subset=["text"]).reset_index(drop=True)

# 2) Balance classes (down-sample to the smallest class)
min_count = df["label"].value_counts().min()
df = (df.groupby("label", group_keys=False)
        .apply(lambda g: g.sample(n=min_count, random_state=42))
        .reset_index(drop=True))

# 3) Stratified split
train, temp = train_test_split(df, test_size=0.30, stratify=df["label"], random_state=42)
val, test   = train_test_split(temp, test_size=0.50, stratify=temp["label"], random_state=42)

# 4) Write JSONL in Tuning Studio format
def to_jsonl(frame, path):
    with path.open("w") as f:
        for _, row in frame.iterrows():
            f.write(json.dumps({
                "input":  f"Categorise the ticket.\nTicket: {row['text']}\nCategory:",
                "output": row["label"],
            }) + "\n")
    print(f"  - {path}  ({len(frame)} rows)")

print("\nWriting JSONL splits:")
to_jsonl(train, DATA_DIR / "train.jsonl")
to_jsonl(val,   DATA_DIR / "val.jsonl")
to_jsonl(test,  DATA_DIR / "test.jsonl")
print("Done.")
