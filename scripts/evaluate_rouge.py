import json
import torch
from transformers import LEDTokenizer, LEDForConditionalGeneration
from rouge_score import rouge_scorer
from tqdm import tqdm

# Load model
model_name = "allenai/led-base-16384"

tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)
model.eval()

# Load MULTI DOCUMENT dataset
data_file = r"C:\Users\rajan\Music\Project 1\data\raw\multidoc_dataset.json"

with open(data_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Test only 20 samples for speed
samples = data[:20]

scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)

scores = {"rouge1": [], "rouge2": [], "rougeL": []}

for sample in tqdm(samples):

    article = sample["input_text"]
    reference = sample["target_text"]

    inputs = tokenizer(
        article,
        return_tensors="pt",
        truncation=True,
        max_length=4096,
        padding="max_length"
    ).to(device)

    # LED needs global attention on first token
    global_attention_mask = torch.zeros_like(inputs["input_ids"])
    global_attention_mask[:, 0] = 1

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            global_attention_mask=global_attention_mask,
            max_length=200,
            num_beams=4
        )

    prediction = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    result = scorer.score(reference, prediction)

    scores["rouge1"].append(result["rouge1"].fmeasure)
    scores["rouge2"].append(result["rouge2"].fmeasure)
    scores["rougeL"].append(result["rougeL"].fmeasure)

print("\nAVERAGE ROUGE SCORES")

print("ROUGE-1:", round(sum(scores["rouge1"]) / len(scores["rouge1"]), 4))
print("ROUGE-2:", round(sum(scores["rouge2"]) / len(scores["rouge2"]), 4))
print("ROUGE-L:", round(sum(scores["rougeL"]) / len(scores["rougeL"]), 4))
