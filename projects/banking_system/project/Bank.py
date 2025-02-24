from Normall_Account import NormalAccount
from Savings_Account import SavingsAccount
from Cheking_Account import CheckingAccount
from authoriting import Authoritize


class Bank:
    def __init__(self, file):
        self.__accounts = {}
        self.file = file

    def addaccounts(self, account_Type, account_holder, account_number, password, **kwargs_):
        if account_Type == 'cheking':
            limit = kwargs_.get('withdrawlimit', 1)
            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': CheckingAccount(account_holder, account_number, password,
                                                                               int(limit), self.file, 'cheking')}
        # return
        if account_Type == 'saving':
            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': SavingsAccount(account_holder, account_number, password,
                                                                              kwargs_.get('intrestrate', 5), self.file,
                                                                              'saving')}
            # return
        if account_Type == 'normall':

            self.__accounts[int(account_number)] = {'password': password,
                                                    'account': NormalAccount(account_holder, account_number, password,
                                                                             self.file, 'normall')}
            # return NormalAccount(account_holder, account_number, password, self.file)


bank1 = Bank("bank_accounts.csv")
account22 = Authoritize.loging_in(bank1.file, 'hi',55,interest_rate=100)
account222= Authoritize.loging_in(bank1.file, 'hello world',989,withdraw_limit=100)
account11 = Authoritize.loging_in(bank1.file, 'me', 1)
print(account222.new_attribute)
#hi


