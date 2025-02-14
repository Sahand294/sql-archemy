import json
with open('products.json', 'r', encoding='utf-8') as file:
    json1 = json.load(file)
for i in json1['categories']:
    for x in i['products']:
        if x['price'] > 1000:
            print(x)
