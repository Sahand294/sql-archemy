import csv
class CsvHandeling:
    @staticmethod
    def reading_products(product_key):
        global product
        data = CsvHandeling.reading()
        for i in data:
            if i['key'] == product_key:
                product = i
        return product
    @staticmethod
    def reading():
        with open('products.csv','r',encoding='utf-8') as text1:
            t = csv.DictReader(text1)
            data = []
            for i in t:
                u = {key:value.strip() for key,value in i.items()}
                data.append(u)
            return data
    @staticmethod
    def adding(product_name,price,quantity,key):
        data = CsvHandeling.reading()
        for i in data:
            if i['key'] == key:
                raise ValueError('that product already exists')
        data.append({'key':key,'name':product_name,'price':price,'stock':quantity})
        with open('products.csv','w',newline="",encoding='utf-8') as file:
            filename = data[0].keys()
            writer = csv.DictWriter(file,fieldnames=filename)
            writer.writeheader()
            writer.writerows(data)
    @staticmethod
    def changing_quantity(key,how_much):
        data  = CsvHandeling.reading()
        for x,i in enumerate(data):
            if i['key'] == key:
                if int(i['stock']) < how_much:
                    raise ValueError('not enough')
                t = int(data[x]['stock'])
                data[x]['stock'] = t-how_much
        with open('products.csv','w',newline="",encoding='utf-8') as file:
            filename = data[0].keys()
            writer = csv.DictWriter(file,fieldnames=filename)
            writer.writeheader()
            writer.writerows(data)