import csv
class Adding_Account:
    def adding(self,id,password):
        with open('accounts.csv','r',encoding='utf-8') as text1:
            r = csv.DictReader(text1)
            data = []
            for i in r:
                file = {key:value.strip() for key,value in i.items()}
                data.append(file)
        e = True
        r = 1
        for i in data:
            if i['id'] == str(id):
                e = False
        if e:
            data.append({'id':int(id),'password':password})
            with open('accounts.csv','w',encoding='utf-8',newline='') as text2:
                file = 'id','password'
                writer = csv.DictWriter(text2,fieldnames=file)
                writer.writeheader()
                writer.writerows(data)