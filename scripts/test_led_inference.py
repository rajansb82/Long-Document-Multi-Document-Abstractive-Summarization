import json
import torch
from transformers import LEDTokenizer, LEDForConditionalGeneration

# Load model and tokenizer
model_name = "allenai/led-base-16384"
tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)

model.eval()

# Load dataset
data_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_model_ready.json"

with open(data_file, "r", encoding="utf-8") as f:
    data = json.load(f)

# Take only 5 samples
samples = data[:5]

for i, sample in enumerate(samples, 1):
    input_text = sample["input_text"][:8000]  # limit length for safety

    inputs = tokenizer(
        input_text,
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

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    print(f"\n===== SAMPLE {i} =====")
    print("MODEL SUMMARY:\n", summary)
    print("\nREFERENCE SUMMARY:\n", sample["target_text"][:500])

