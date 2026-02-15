
import json
import re
from datetime import datetime

input_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset.json"
output_file = r"C:\Users\rajan\Music\Project 1\data\raw\dataset_clean.json"

def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = re.sub(r"<.*?>", "", text)   # remove HTML
    text = re.sub(r"\s+", " ", text)    # normalize spaces
    return text.strip()

with open(input_file, "r", encoding="utf-8") as f:
    data = json.load(f)

cleaned = []

for row in data:
    article = clean_text(row.get("article_text", ""))
    summary = clean_text(row.get("human_summary", ""))
    
    if len(article) < 200 or len(summary) < 50:
        continue

    cleaned.append({
        "newspaper": row.get("newspaper_name", "").strip(),
        "date": row.get("published_date\n", "").strip(),
        "headline": clean_text(row.get("headline", "")),
        "article_text": article,
        "summary": summary,
        "category": row.get("news_category", "").strip()
    })

with open(output_file, "w", encoding="utf-8") as f:
    json.dump(cleaned, f, indent=2, ensure_ascii=False)

print("Cleaned records:", len(cleaned))
print("Saved to:", output_file)
