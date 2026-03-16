import json
import torch
from transformers import LEDTokenizer, LEDForConditionalGeneration

# Load LED model
model_name = "allenai/led-base-16384"

tokenizer = LEDTokenizer.from_pretrained(model_name)
model = LEDForConditionalGeneration.from_pretrained(model_name)

model.eval()

# Load MULTI DOCUMENT dataset
data_file = "../raw/multidoc_dataset.json"

with open(data_file,"r",encoding="utf-8") as f:
    data = json.load(f)

print("Total samples:",len(data))

# Test only first 5 samples
samples = data[:5]

for i,sample in enumerate(samples):

    article = sample["input_text"]

    inputs = tokenizer(
        article,
        max_length=4096,
        truncation=True,
        return_tensors="pt"
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            max_length=200,
            num_beams=4
        )

    summary = tokenizer.decode(summary_ids[0],skip_special_tokens=True)

    print("\n---------------------------")
    print("INPUT (MULTI DOC):")
    print(article[:500])
    print("\nMODEL SUMMARY:")
    print(summary)
    print("\nREFERENCE SUMMARY:")
    print(sample["target_text"])
