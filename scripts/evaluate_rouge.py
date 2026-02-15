
import json
import torch
from transformers import LEDTokenizer, LEDForConditionalGeneration
from rouge_score import rouge_scorer

model_name = "allenai/led-base-16384"
tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)
model.eval()

data_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_model_ready.json"

with open(data_file, "r", encoding="utf-8") as f:
    data = json.load(f)

samples = data[:10]  # only 10 samples for speed

scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)

scores = {"rouge1": [], "rouge2": [], "rougeL": []}

for sample in samples:
    inputs = tokenizer(
        sample["input_text"][:8000],
        return_tensors="pt",
        truncation=True,
        max_length=4096
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=200,
            num_beams=4
        )

    pred = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    ref = sample["target_text"]

    result = scorer.score(ref, pred)

    for k in scores:
        scores[k].append(result[k].fmeasure)

print("\nAVERAGE ROUGE SCORES:")
for k in scores:
    print(k, round(sum(scores[k]) / len(scores[k]), 4))

