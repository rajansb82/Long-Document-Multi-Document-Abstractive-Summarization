import json
from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
with open("../raw/dataset_model_ready.json","r",encoding="utf-8") as f:
    data = json.load(f)

articles = [item["input_text"] for item in data]

print("Total articles:",len(articles))
model = SentenceTransformer("all-MiniLM-L6-v2")

embeddings = model.encode(articles,show_progress_bar=True)
num_clusters = 30

kmeans = KMeans(n_clusters=num_clusters,random_state=42)
labels = kmeans.fit_predict(embeddings)
clusters = {}

for i,label in enumerate(labels):

    if label not in clusters:
        clusters[label] = []

    clusters[label].append(data[i])
with open("../raw/dataset_multidoc.json","w",encoding="utf-8") as f:
    json.dump(clusters,f,indent=2)

print("Clusters created:",len(clusters))
