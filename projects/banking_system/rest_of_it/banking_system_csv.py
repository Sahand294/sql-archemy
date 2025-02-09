import csv


class BankAccount:
    def __init__(self, bank_holder, account_number, password):
        self.bank_holder = bank_holder
        self.account_number = account_number
        self.password = password
        self.total_Review = {'owner': self.bank_holder, 'id': self.account_number, 'balance': self.check_money()}

        with open("bank_account.csv", 'r', encoding="utf-8") as text1:
            if f"{account_number}" in text1.read():
                pass
            else:
                with open("bank_account.csv", 'a', encoding="utf-8") as text:
                    text.write(f'\n{self.total_Review}')

    def check_money(self):
        with open("bank_account.csv", 'r', encoding="utf-8") as text1:
            r = csv.DictReader(text1)
            data = []
            for i in r:
                file = {key: value.strip() for key, value in i.items()}
                data.append(file)
            for i in data:
                if i["id"] == str(self.account_number):
                    balance = i["balance"]
            return float(balance)

    def deposit(self, money, address_file: str):

        with open(address_file, 'r', encoding="utf-8") as file:
            r = csv.DictReader(file)
            data = []
            for i in r:
                files = {key: value.strip() for key, value in i.items()}
                data.append(files)
        for x, i in enumerate(data):
            if i['id'] == str(self.account_number):
                data[x]['balance'] = float(data[x]['balance']) + money
        with open(address_file, "w", encoding="utf-8", newline="") as text:
            file = data[0].keys()
            writer = csv.DictWriter(text, fieldnames=file)
            writer.writeheader()
            writer.writerows(data)

        with open(f"transaction", 'a') as text:
            text.write(f'\n{self.account_number} has deposited {money}$  balance:{self.check_money()}')

    def check_password(self):
        with open("bank_account.csv", 'r', encoding="utf-8") as text1:
            r = csv.DictReader(text1)
            data = []
            for i in r:
                file = {key: value.strip() for key, value in i.items()}
                data.append(file)
            for i in data:
                if i["id"] == str(self.account_number):
                    balance = i["password"]
            return str(balance)

    def withrawing(self, money, password):

        if password != self.check_password():
            raise ValueError("its incorrect")
        if self.check_money() >= money:
            pass
        else:
            raise ValueError(f'not enough money')
        print('withdraw implementing subclass')
        with open(f"transaction", 'a') as text:
            text.write(f'\n{self.account_number} has withdraw {money}$  balance:{self.check_money()}')

        with open("bank_account.csv", 'r', encoding="utf-8") as file:
            r = csv.DictReader(file)
            data = []
            for i in r:
                files = {key: value.strip() for key, value in i.items()}
                data.append(files)
        for x, i in enumerate(data):
            if i['id'] == str(self.account_number):
                data[x]['balance'] = float(data[x]['balance']) - money
        with open("bank_account.csv", "w", encoding="utf-8", newline="") as text:
            file = data[0].keys()
            writer = csv.DictWriter(text, fieldnames=file)
            writer.writeheader()
            writer.writerows(data)

    def transfer(self, money, target_account, password, account_file):

        if not isinstance(target_account, BankAccount) or isinstance(target_account, SavingsAccount):
            raise ValueError(f'the account {target_account} does not exist')

        with open(f"transaction", 'a') as text:
            text.write(
                f'\n{self.account_number} has transferred {money}$ from {self.account_number} to {target_account} balance:{self.check_money()}')

        self.withrawing(money, password)
        target_account.deposit(money, account_file)

        with open(f"transaction", 'a') as text:
            text.write(
                f'\n{self.account_number} has transferred {money}$ from {self.account_number} to {target_account} balance:{self.check_money()}')

    def review(self):
        return {'owner': self.bank_holder, 'id': self.account_number, 'balance': self.check_money()}


class NormalAccount(BankAccount):
    pass


class SavingsAccount(BankAccount):
    def __init__(self, bank_holder, account_Number, password, intrest_Rate):
        self.total_Review = {'owner': bank_holder, 'id': account_Number, 'balance': 0.0, 'type': 'savings',
                             'interest rate': intrest_Rate}
        super().__init__(bank_holder, account_Number, password)
        self.intrestrate = intrest_Rate

    def applyintrest(self, account_file):
        self.deposit(self.check_money() * (self.intrestrate / 100.0), account_file)


class CheckingAccount(BankAccount):
    def __init__(self, account_holder, account_number, password, withdrawlimit):
        self.total_Review = {'owner': account_holder, 'id': account_number, 'balance': 0.0, 'type': 'checking',
                             'withdraw limit': withdrawlimit}
        super().__init__(account_holder, account_number, password)
        self.limit = withdrawlimit

    def withrawing(self, money, password):
        if self.limit < money:
            raise Exception(f"you have hit the withdraw limit")
        super().withrawing(money, password)


class Bank:
    def __init__(self):
        self.accounts = {}

    def addaccounts(self, account_Type, account_holder, account_number, password, **kwargs_):
        if account_Type == 'cheking':
            account = CheckingAccount(account_holder, account_number, password, kwargs_.get('withdrawlimit', 500))
        if account_Type == 'saving':
            account = SavingsAccount(account_holder, account_number, password, kwargs_.get('intrestrate', 5))
        if account_Type == 'normall':
            account = NormalAccount(account_holder, account_number, password)
        self.accounts[account_number] = account

    def authenticate(self, account_numbers, password):
        id = account_numbers
        if account_numbers not in self.accounts:
            raise ValueError(f'there is no such account!')

        if password != self.accounts[id]['password']:
            raise ValueError(f'incorrect password')
        account = self.accounts


account1 = SavingsAccount(55, 95849, 'hey', 100)

account2 = CheckingAccount('sahand', 989, 'hello world', 500)

account1.deposit(100,"bank_account.csv")
