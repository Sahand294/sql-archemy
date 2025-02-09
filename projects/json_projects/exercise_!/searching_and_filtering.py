import json

with open('store.json', 'r', encoding='utf-8') as text:
    json1 = json.load(text)
    text1 = text
filtered = []
for x, i in enumerate(json1['products']):
    if i['brand'] == "BrandA":
        if i['price'] > 1000:
            filtered.append(i)
print(filtered)
json1['products'].append({"id": 7, "name": "Ali", "brand": "ali@example.com", "price": 25})

with open('store.json', 'w') as file:
    json.dump(json1, file, indent=4)
