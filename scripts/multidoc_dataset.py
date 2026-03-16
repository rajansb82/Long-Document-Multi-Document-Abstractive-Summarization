import json

with open("../raw/multidoc_clusters.json","r",encoding="utf-8") as f:
    clusters = json.load(f)

dataset = []

for category,items in clusters.items():

    docs = []

    for article in items[:5]:
        docs.append(article["input_text"])

    input_text = "\n\n".join(docs)

    summary = items[0]["target_text"]

    dataset.append({
        "input_text":input_text,
        "target_text":summary
    })

with open("../raw/multidoc_dataset.json","w",encoding="utf-8") as f:
    json.dump(dataset,f,indent=2)

print("Multi document dataset created")
