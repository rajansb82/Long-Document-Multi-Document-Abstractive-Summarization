import json
import numpy as np
from collections import Counter

# Load dataset
path = "../raw/dataset_model_ready.json"

with open(path,"r",encoding="utf-8") as f:
    data = json.load(f)

print("\nDATASET ANALYSIS\n")

total_samples = len(data)

article_lengths = []
summary_lengths = []

all_tokens = []

for item in data:

    article = item["input_text"]
    summary = item["target_text"]

    article_words = article.split()
    summary_words = summary.split()

    article_lengths.append(len(article_words))
    summary_lengths.append(len(summary_words))

    all_tokens.extend(article_words)

print("Total Samples:", total_samples)


print("\nARTICLE STATS")

print("Average Length:", round(np.mean(article_lengths),2))
print("Median Length:", np.median(article_lengths))
print("Min Length:", np.min(article_lengths))
print("Max Length:", np.max(article_lengths))
print("Std Dev:", round(np.std(article_lengths),2))


print("\nSUMMARY STATS")

print("Average Length:", round(np.mean(summary_lengths),2))
print("Median Length:", np.median(summary_lengths))
print("Min Length:", np.min(summary_lengths))
print("Max Length:", np.max(summary_lengths))
print("Std Dev:", round(np.std(summary_lengths),2))

compression_ratio = np.mean(article_lengths) / np.mean(summary_lengths)

print("\nCompression Ratio:", round(compression_ratio,2))

vocab = set(all_tokens)

total_tokens = len(all_tokens)
vocab_size = len(vocab)

ttr = vocab_size / total_tokens

print("\nVOCABULARY")

print("Total Tokens:", total_tokens)
print("Vocabulary Size:", vocab_size)
print("Type Token Ratio:", round(ttr,4))



counter = Counter(all_tokens)

print("\nTOP 10 WORDS")

for word,count in counter.most_common(10):
    print(word,"-",count)

print("\nANALYSIS COMPLETE")
