import json
from collections import Counter

file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_with_category.json"

with open(file,"r",encoding="utf-8") as f:
    data=json.load(f)

domains=[item["category"] for item in data]

count=Counter(domains)

print("\nDOMAIN DISTRIBUTION\n")

for k,v in count.items():
    print(k,"-",v)
