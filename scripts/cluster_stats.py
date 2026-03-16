import json
import numpy as np

file=r"C:\Users\rajan\Music\Project 1\data\raw\multidoc_dataset.json"

with open(file,"r",encoding="utf-8") as f:
    data=json.load(f)

docs_per_cluster=[]

for item in data:
    docs=len(item["input_text"].split("\n\n"))
    docs_per_cluster.append(docs)

print("\nCLUSTER STATS")

print("Average docs per cluster:",round(np.mean(docs_per_cluster),2))
print("Min docs:",min(docs_per_cluster))
print("Max docs:",max(docs_per_cluster))
