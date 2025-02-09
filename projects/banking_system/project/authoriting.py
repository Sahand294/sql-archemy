import csv
from Cheking_Account import CheckingAccount
from Savings_Account import SavingsAccount
from Normall_Account import NormalAccount

c = CheckingAccount
n = NormalAccount
s = SavingsAccount


class Authoritize:
    @staticmethod
    def loging_in(files, password, id, **kwargs_):
        with open(files, 'r', encoding='utf-8') as file:
            f = csv.DictReader(file)
            data = []
            for x in f:
                data.append({key: value.strip() for key, value in x.items()})
        error = True
        for i in data:
            if i['id'] == str(id):
                u = i
                error = False
        if error:
            raise ValueError('no such account')
        if password != u['password']:
            raise ValueError('wrong password')
        if u['type'] == 'cheking':
            if 'withdraw_limit' not in kwargs_:
                raise ValueError('you have to give the withdraw limit')
            r = c(u['owner'], u['id'], u['password'], int(kwargs_.get('withdraw_limit')), files, 'cheking')
        elif u['type'] == 'saving':

            if 'interest_rate' not in kwargs_:
                raise ValueError('you have to give the interest rate')

            r = s(u['owner'], u['id'], u['password'], int(kwargs_.get('interest_rate')), files, 'saving')
        elif u['type'] == 'normall':
            r = n(u['owner'], u['id'], u['password'], files, 'normall')
        else:
            raise ValueError('no such type')
        return r
