print("PRIMERA SCRIPT STARTED", flush=True)

import os
import json
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "allenai/PRIMERA"
DATA_PATH = "data/raw/dataset_multidoc.json"
OUTPUT_PATH = "results/primera/predictions.json"

os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)

device = "cuda" if torch.cuda.is_available() else "cpu"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME).to(device)

with open(DATA_PATH, "r", encoding="utf-8") as f:
    data = json.load(f)

print(f"Loaded records: {len(data)}", flush=True)

predictions = []

for i, item in enumerate(data[:10]):
    docs = item.get("documents") or item.get("articles") or item.get("texts") or []
    if not docs:
        continue

    input_text = " </s> ".join(docs)

    inputs = tokenizer(
        input_text,
        truncation=True,
        padding="max_length",
        max_length=4096,
        return_tensors="pt"
    ).to(device)

    summary_ids = model.generate(
        **inputs,
        max_length=256,
        num_beams=4
    )

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    predictions.append({
        "cluster_id": item.get("cluster_id"),
        "generated_summary": summary,
        "reference_summary": item.get("human_summary")
    })

    print(f"Processed {i}", flush=True)

with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
    json.dump(predictions, f, indent=2)

print("PRIMERA inference completed", flush=True)

