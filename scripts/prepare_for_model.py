
import json


input_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_multidoc.json"
output_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_model_ready.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

model_data = []

for cluster in data:
    articles = []
    for doc in cluster["documents"]:
        if "article_text" in doc:
            articles.append(doc["article_text"])

    if len(articles) == 0:
        continue

    input_text = " ".join(articles)
    target_text = cluster["summary"]

    model_data.append({
        "input_text": input_text,
        "target_text": target_text
    })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(model_data, f, indent=2, ensure_ascii=False)

print("Model-ready samples:", len(model_data))
print("Saved to:", output_file)

