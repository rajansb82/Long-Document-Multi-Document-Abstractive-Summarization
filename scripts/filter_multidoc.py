import json

input_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_clustered.json"
output_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_multidoc.json"

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

multidoc = [c for c in data if len(c["documents"]) >= 2]

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(multidoc, f, indent=2, ensure_ascii=False)

print("Multi-doc clusters:", len(multidoc))
print("Saved to:", output_file)

