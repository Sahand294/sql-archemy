import csv
class Passwords:
    def check_password(self, password,id):
        with open('accounts.csv', 'r', encoding='utf-8') as text:
            r = csv.DictReader(text)
            data = []
            for i in r:
                data.append({key: value.strip() for key, value in i.items()})
            for i in data:
                if i['id'] == str(id):
                    if i['password'] == str(password):
                        return True
                    else:
                        return False
                else:
                    raise ValueError('no such account')
    def change_password(self,id,new_password):
        with open('accounts.csv','r',encoding='utf-8') as text1:
            r = csv.DictReader(text1)
            date = []
            for i in r:
                date.append({key: value.strip() for key, value in i.items()})
        for x,i in enumerate(date):
            if i['id'] == str(id):

                date[x]['password'] = new_password
        with open('accounts.csv','w',encoding='utf-8',newline='') as text2:

            file = date[0].keys()
            writer = csv.DictWriter(text2,fieldnames=file)
            writer.writeheader()
            writer.writerows(date)

