import csv

with open("hey.csv", 'r', encoding="utf-8") as csvfile:
    r = csv.DictReader(csvfile)
    data = []
    for i in r:
        cr = {key: value.strip() for key, value in i.items()}
        #cr = {}
        #for key,value in i.items():
         #   cr[key] = value.strip()
        data.append(cr)
data[4]["name"] = "radaman"

with open("hey.csv", 'w', encoding="utf-8", newline="") as text:
    filename = data[0].keys()
    writer = csv.DictWriter(text, fieldnames=filename)
    writer.writeheader()
    writer.writerows(data)
