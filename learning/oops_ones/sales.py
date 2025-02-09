recid = []
class UserInfo:
    def __init__(self, name, address):
        global  recid1
        self.name = name
        self.ip = address
        names = input('whats the name of the product:')
        prices = input('how much does it cost:')
        amount = input('how much:')
        ProductInfo(names, prices, amount, name, address)
        recid1 = f'{name},ip:{address}'


class ProductInfo:
    def __init__(self, name, price, quantity, username, address):
        self.producname = name
        self.price = price
        self.amount = quantity
        CalculatorOfProductInfo(self.price, self.producname, self.amount, username, address)


class CalculatorOfProductInfo:
    def __init__(self, price, name, amounttobepurchosed, username, address):
        self.paycheck = int(price) * int(amounttobepurchosed)
        self.productname = name
        CheckMaker(self.paycheck, amounttobepurchosed, name, username, address)


class CheckMaker:
    def __init__(self, payamount, amountofproduct, name, username, address):
            recid.append(f'has bought:{name}:amount:{amountofproduct},total amount:{payamount}')
meh = int(input('how many purchuses:'))
for i in range(meh):
    user1 = UserInfo('sahand', 'st.johns')
print(recid1,recid)
