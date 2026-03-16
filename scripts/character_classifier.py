import json
with open("../raw/dataset_model_ready.json","r",encoding="utf-8") as f:
    data = json.load(f)

categories = {
"politics":["government","parliament","minister","election","policy"],
"business":["company","market","stock","industry"],
"sports":["match","team","player","tournament","league"],
"technology":["technology","software","AI","internet","device"],
"health":["hospital","health","virus","disease","medical"],
"crime":["police","court","arrest","investigation"],
"world":["country","international","global","foreign"]
}

for item in data:
    
    text = item["input_text"].lower()
    item["category"] = "other"

    for cat,keywords in categories.items():
        for k in keywords:
            if k in text:
                item["category"] = cat
                break
with open("../raw/dataset_with_category.json","w",encoding="utf-8") as f:
    json.dump(data,f,indent=2)

print("Category mapping completed")
