
import pandas as pd
import nltk
from rouge_score import rouge_scorer

nltk.download("punkt")

print("CATEGORY-AWARE LEAD BASELINE STARTED", flush=True)

df = pd.read_csv("data/cleaned/val.csv").head(500)

def category_lead(article, category):
    sentences = nltk.sent_tokenize(str(article))
    
    if category in ["Sports", "Entertainment"]:
        k = 2
    elif category in ["Politics", "Business"]:
        k = 4
    else:
        k = 3

    return " ".join(sentences[:k])

preds, refs = [], []

for _, row in df.iterrows():
    preds.append(category_lead(row["Article"], str(row["Category"])))
    refs.append(row["Summary"])

scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)

r1 = r2 = rl = 0.0

for p, r in zip(preds, refs):
    s = scorer.score(r, p)
    r1 += s["rouge1"].fmeasure
    r2 += s["rouge2"].fmeasure
    rl += s["rougeL"].fmeasure

n = len(preds)
print("ROUGE-1:", r1 / n)
print("ROUGE-2:", r2 / n)
print("ROUGE-L:", rl / n)

print("CATEGORY-AWARE LEAD BASELINE COMPLETED")
