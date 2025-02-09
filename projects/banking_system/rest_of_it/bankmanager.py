class Bank:
    def get_account(self, id):
        if id not in self.__accounts:
            raise KeyError('no such account!')
        return id
    def __init__(self):
        self.__accounts = {}

    def AddAcounts(self, money, acount_holder, id):
        if id in self.__accounts:
            raise ValueError(f'the id:{id} already exist')
        self.__accounts[id] = {'amount_of_money': money, 'owner': acount_holder, 'id': id}
        return self.__accounts[id]
    def Depositing(self, id, amount_of_money):
        self.get_account(id)
        self.__accounts[id]['amount_of_money'] += amount_of_money
        return f'we have succesfully deposited {amount_of_money} in the acount{id} owned by {self.__accounts[id]['owner']} and now the account has {self.__accounts[id]['amount_of_money']}'

    def withdrawing(self, id, amount_of_money):
        self.get_account(id)
        if self.__accounts[id]['amount_of_money'] < amount_of_money:
            raise KeyError('no enouth money')
        self.__accounts[id]['amount_of_money'] -= amount_of_money
        return f'we have succesfully withdrawed  {amount_of_money} from the account:{id} owned by {self.__accounts[id]['owner']} and now the account has {self.__accounts[id]['amount_of_money']}'



    def transfer(self, the_id_of_the_acount_money_going_from, the_id_of_the_acount_money_going_in_to, amount_of_money):
        from_account = self.get_account(the_id_of_the_acount_money_going_from)
        to_Account = the_id_of_the_acount_money_going_in_to

        if self.__accounts[from_account]['amount_of_money'] < amount_of_money:
            raise KeyError('not enough money')
        self.Depositing(to_Account, amount_of_money)
        self.withdrawing(from_account, amount_of_money)
        return f'we have succesfully transfered  {amount_of_money} from the account:{from_account} in the account:{to_Account} and now the account has {self.__accounts[from_account]['amount_of_money']}, and now the other account has {self.__accounts[to_Account]['amount_of_money']}'

    def Review_all(self):
        return self.__accounts

    def Review_one(self, id):
        if id in self.__accounts:
            return self.__accounts[id]
        else:
            raise KeyError(f'no such account as {id}')



cibc = Bank()
acount1 = cibc.AddAcounts(500, 'sahand', 8832858)
account2 = cibc.AddAcounts(300, 'sahand', 993845)
a
print(cibc.transfer(8832858, 993845, 200))
print(cibc.Review_all())
