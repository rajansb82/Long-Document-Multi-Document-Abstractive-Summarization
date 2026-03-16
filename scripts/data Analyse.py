import pandas as pd

print("DATA ANALYSIS STARTED", flush=True)

df = pd.read_csv("data/cleaned/NewsSumm_Cleaned.csv")

print("Total samples:", len(df), flush=True)
print("Columns:", df.columns.tolist(), flush=True)

df["Article_Length"] = df["Article"].astype(str).str.split().str.len()
df["Summary_Length"] = df["Summary"].astype(str).str.split().str.len()

print("Average Article Length:", df["Article_Length"].mean(), flush=True)
print("Average Summary Length:", df["Summary_Length"].mean(), flush=True)

print("Max Article Length:", df["Article_Length"].max(), flush=True)
print("Max Summary Length:", df["Summary_Length"].max(), flush=True)

print("DATA ANALYSIS COMPLETED", flush=True)
