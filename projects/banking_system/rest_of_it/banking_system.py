import ast
import csv

class BankAccount:
    def __init__(self, bank_holder, account_number, password):
        self.balance = 0.0
        self.bank_holder = bank_holder
        self.account_number = account_number
        self.password = password
        self.transactions = []
        self.total_Review = {'owner': self.bank_holder, 'id': self.account_number, 'balance': self.balance}

        with open("accounts.txt", 'r') as text1:
            if f"{account_number}" in text1.read():
                pass
            else:
                with open("accounts.txt", 'a') as text:
                    text.write(f'\n{self.total_Review}')

    def check_money(self):
        with open("accounts.txt", 'r') as text1:
            lines = text1.readlines()
            for y, i in enumerate(lines):
                x = ast.literal_eval(i.strip())
                if x['id'] == self.account_number:
                    balance = x['balance']
                    return balance

    def deposit(self, money):
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

    def withrawing(self, money, password):

        if password != self.password:
            raise ValueError("its incorrect")
        if self.check_money() >= money:
            self.balance -= money
        else:
            raise ValueError(f'not enough money')
        print('withdraw implementing subclass')
        with open(f"transaction", 'a') as text:
            text.write(f'\n{self.account_number} has withdraw {money}$  balance:{self.balance}')

        update_line = []
        line = 1
        with open("accounts.txt", 'r') as text1:
            lines = text1.readlines()
            for y, i in enumerate(lines):
                x = ast.literal_eval(i.strip())
                x['balance'] -= money
                if x['id'] == self.account_number:
                    lines[y] = x
                if line == 1:
                    update_line.append(f'{str(lines[y])}')
                    line -= 1
                else:
                    update_line.append(f'\n{str(lines[y])}')
            with open("accounts.txt", 'w') as text2:
                text2.writelines(update_line)

    def transfer(self, money, target_account, password):
        if password != self.password:
            raise ValueError("its incorrect")

        if not isinstance(target_account, BankAccount) or isinstance(target_account, SavingsAccount):
            raise ValueError(f'the account {target_account} does not exist')

        with open(f"transaction", 'a') as text:
            text.write(
                f'\n{self.account_number} has transferred {money}$ from {self.account_number} to {target_account} balance:{self.balance}')

        self.withrawing(money, password)
        update_line = []
        line = 1
        with open("accounts.txt", 'r') as text1:
            lines = text1.readlines()
            for y, i in enumerate(lines):
                x = ast.literal_eval(i.strip())
                x['balance'] += money
                if x['id'] == target_account.account_number:
                    lines[y] = x
                if line == 1:
                    update_line.append(f'{str(lines[y])}')
                    line -= 1
                else:
                    update_line.append(f'{str(lines[y])}')
            with open("accounts.txt", 'w') as text2:
                text2.writelines(update_line)

    def review(self):
        return {'owner': self.bank_holder, 'id': self.account_number, 'balance': self.balance}


class NormallAccount(BankAccount):
    pass


class SavingsAccount(BankAccount):
    def __init__(self, bank_holder, account_Number, password, intrest_Rate):
        self.total_Review = {'owner': bank_holder, 'id': account_Number, 'balance': 0.0, 'type': 'savings',
                             'interest rate': intrest_Rate}
        super().__init__(bank_holder, account_Number, password)
        self.intrestrate = intrest_Rate

    def applyintrest(self):
        self.deposit(self.balance * (self.intrestrate / 100.0))


class Checking(BankAccount):
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
            account = Checking(account_holder, account_number, password, kwargs_.get('withdrawlimit', 500))
        if account_Type == 'saving':
            account = SavingsAccount(account_holder, account_number, password, kwargs_.get('intrestrate', 5))
        if account_Type == 'normall':
            account = NormallAccount(account_holder, account_number, password)
        self.accounts[account_number] = account

    def authenticate(self, account_numbers, password):
        account = self.accounts


account1 = NormallAccount(55, 95849, 'hey')

account2 = Checking('sahand', 98955958539485, 'hello world', 500)
account1.deposit(10)
