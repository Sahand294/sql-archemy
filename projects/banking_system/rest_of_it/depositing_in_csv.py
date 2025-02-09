import csv

with open("bank_account.csv", 'r', encoding="utf-8") as file:
    r = csv.DictReader(file)
    data = []
    for i in r:
        files = {key: value.strip() for key, value in i.items()}
        data.append(files)
for x,i in enumerate(data):
    if i['id'] == "95849":
        print(i['balance'])
        data[x]['balance'] = float(data[x]['balance'])+1000
with open("bank_account.csv", "w", encoding="utf-8", newline="") as text:
    file = data[0].keys()
    writer = csv.DictWriter(text, fieldnames=file)
    writer.writeheader()
    writer.writerows(data)






















































#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!1
if self.balance < 0:
    raise ValueError(f'can not add negetive numbers!')
else:
    self.balance += money
with open(f"transaction", 'a') as text:
    text.write(f'\n{self.account_number} deposited {money}$ balance:{self.balance}')

update_line = []
line = 1
with open("accounts.txt", 'r') as text1:
    lines = text1.readlines()
    for y, i in enumerate(lines):
        x = ast.literal_eval(i.strip())
        x['balance'] += money
        if x['id'] == self.account_number:
            lines[y] = x
        if line == 1:
            update_line.append(f'{str(lines[y])}')
            line -= 1
        else:
            update_line.append(f'\n{str(lines[y])}')
    with open("accounts.txt", 'w') as text2:
        text2.writelines(update_line)