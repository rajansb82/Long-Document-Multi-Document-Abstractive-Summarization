import json
import hashlib

input_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_clean.json"
output_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_clustered.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

clusters = {}

for row in data:
    key = f"{row['category']}_{row['date']}_{row['headline'][:50]}"
    cluster_id = hashlib.md5(key.encode()).hexdigest()

    if cluster_id not in clusters:
        clusters[cluster_id] = {
            "cluster_id": cluster_id,
            "category": row["category"],
            "date": row["date"],
            "summary": row["summary"],
            "documents": []
        }

    clusters[cluster_id]["documents"].append({
        "headline": row["headline"],
        "article_text": row["article_text"],
        "newspaper": row["newspaper"]
    })

clustered_data = list(clusters.values())

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(clustered_data, f, indent=2, ensure_ascii=False)

print("Total clusters:", len(clustered_data))
print("Saved to:", output_file)

