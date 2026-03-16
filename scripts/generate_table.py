import json
import numpy as np

file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_model_ready.json"

with open(file,"r",encoding="utf-8") as f:
    data=json.load(f)

article_lengths=[]
summary_lengths=[]

for item in data:
    article_lengths.append(len(item["input_text"].split()))
    summary_lengths.append(len(item["target_text"].split()))

print("\nDATASET SCALE")
print("Total Articles:",len(data))
print("Total Summaries:",len(data))

print("\nARTICLE LENGTH")
print("Average:",round(np.mean(article_lengths),2))
print("Median:",np.median(article_lengths))
print("Min:",min(article_lengths))
print("Max:",max(article_lengths))

print("\nSUMMARY LENGTH")
print("Average:",round(np.mean(summary_lengths),2))
print("Min:",min(summary_lengths))
print("Max:",max(summary_lengths))

compression = np.mean(article_lengths)/np.mean(summary_lengths)

print("\nCOMPRESSION RATIO:",round(compression,2))
