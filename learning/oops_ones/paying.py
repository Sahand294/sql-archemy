paypal = False
creditcard = False


class Info:
    def __init__(self, creditway, amount_to_be_paid):
        self.waypay = creditway
        self.money = amount_to_be_paid

class FiguringOut:
    def __init__(self,info):
        if info.waypay == 'paypal':
            Paypal('hassan@gmail.com',info)
        if info.waypay == 'credit card' or info.waypay == 'creditcard':
            CreditCard(135335,info)
class Paypal:
    def __init__(self, email,info):
        global paypal
        self.email = email
        paypal = True
        FailOrSucces(info)


class CreditCard:
    def __init__(self, id_number,info):
        global creditcard
        self.id = id_number
        creditcard = True
        FailOrSucces(info)


class FailOrSucces:

    def __init__(self,info):
        global paypal,creditcard
        if paypal:
            if info.money >= 4000:
                raise Exception('the amount to be paid is way to much pall.')
            print(f'payment for paypal success with {info.money} removed')
            paypal = False
        if creditcard:
            if info.money >= 1001:
                raise Exception('the amount to be paid is way to much for credit card.')
            print(f'payment for credit card success with {info.money} removed')
            creditcard = False



inf = Info('creditcard',1000)
FiguringOut(inf)

infoo = Info('paypal',2000)
FiguringOut(infoo)
