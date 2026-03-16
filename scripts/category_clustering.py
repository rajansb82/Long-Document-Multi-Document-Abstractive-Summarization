import json
from collections import defaultdict

with open("../raw/dataset_with_category.json","r",encoding="utf-8") as f:
    data = json.load(f)

clusters = defaultdict(list)

for item in data:
    clusters[item["category"]].append(item)

print("Total clusters:",len(clusters))

for c in clusters:
    print(c,len(clusters[c]))

with open("../raw/multidoc_clusters.json","w",encoding="utf-8") as f:
    json.dump(clusters,f,indent=2)
