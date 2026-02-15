import json

file_path = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_clustered.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

num_clusters = len(data)
doc_counts = [len(c["documents"]) for c in data]

print("Total clusters:", num_clusters)
print("Average docs per cluster:", round(sum(doc_counts) / num_clusters, 2))
print("Max docs in a cluster:", max(doc_counts))
print("Clusters with >= 2 docs:", sum(1 for x in doc_counts if x >= 2))

