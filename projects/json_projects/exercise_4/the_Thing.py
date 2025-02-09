import json
import zlib
strjson =   [
    {"id": 1, "name": "Product A", "price": 10.99},
    {"id": 2, "name": "Product B", "price": 20.49},
    {"id": 3, "name": "Product C", "price": 15.29}
]
with open('product.json','w') as file:
    json.dump(strjson,file)
with open('product.json','r',encoding='utf-8') as text:
    json1 = text.read()
#print(json1)
compressed_json = zlib.compress(json1.encode())
#print(compressed_json)
with open('compressed.json.zlib','wb') as file:
    file.write(compressed_json)
with open('compressed.json.zlib','rb') as file:
    f = file.read()
x = zlib.decompress(f).decode()
#print(x)
y = json.loads(x)
print(y[1]['price'])