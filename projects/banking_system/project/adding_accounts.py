import csv


class Adding_Accounts:
    field_names = 'owner,id,balance'
    def adding_account(self, account_file, account_number, bank_holder,password,type):
        field_names = 'owner,id,balance'
        try:
            with open(account_file, 'r', encoding="utf-8") as text:
                if f"{account_number}" in text.read():
                    pass
                else:
                    with open(account_file, 'a', encoding="utf-8") as file:

                        file.write(f'\n{bank_holder},{account_number},{password},0.0,{type}')

        except:
            with open(account_file, 'w', encoding='utf-8',newline="") as text:
                text.write('owner,id,password,balance')
                text.write(f'\n{bank_holder},{account_number},{password},0.0')
               # writer = csv.DictWriter(text, fieldnames=field_names)
                #writer.writeheader()
                #writer.writerow(f'\n{bank_holder},{account_number},0.0')
