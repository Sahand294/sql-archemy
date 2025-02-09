stored = {'stock':{'clothes':18
                   ,'toys':55
                   ,'books':25},
          'price': {'clothes':12
              , 'toys': 5
              , 'books': 9
                    }}
print('this is the old store:',stored,'\n')
class Ading:
    def __init__(self):
        for i in range(len(stored)):
            stored['stock']['laptop'] = 18
            stored['stock']['mouse'] = 50
            stored['price']['laptop'] = 850
            stored['price']['mouse'] = 20


class discounter(Ading):
    def discounts(self=1):
        for i in stored['price']:
            stored['price'][i] = stored['price'][i]/2
Ading()
print('this is the store with new products:',stored,'\n')

discounter.discounts()

print('this is the store with discounts:',stored,'\n')