class Customer:
    def __init__(self,name,email,mebershipdate,list):
        self.name = name
        self.email = email
        self.meberdate = mebershipdate
        self.list = list
        list[name] = {'name':name,'email':email,'membership date':mebershipdate,'last purchase':'0'}
    def purchase(self,purchasedate):
        self.purchase = purchasedate
        self.list[self.name]['last purchase'] = self.purchase

class Search:
    def name(self,list,name):
        self.name = name
        self.list = list
        print(list[name])
    def membership(self,list,date):
        for i in list:
            if list[i]['membership date'] == date:
                print(list[i])

    def purchase(self,list,purchase):
        for i in list:
            if list[i]['last purchase'] == purchase:
                print(list[i])

custumers = {}
custumer1 = Customer('Emma','emma@example','2022-11-13',custumers)
custumer1.purchase('2024-11-18')

customer2 = Customer('Alice', 'alice.wonderland@example.com', '2023-06-25', custumers)
customer2.purchase('2025-07-12')

customer3 = Customer('Bob', 'bob.builder@example.com', '2021-04-10', custumers)
customer3.purchase('2024-09-03')

customer4 = Customer('Charlie', 'charlie.chocolate@example.com', '2022-08-19', custumers)
customer4.purchase('2025-11-25')

customer5 = Customer('Diana', 'diana.prince@example.com', '2020-12-01', custumers)
customer5.purchase('2023-05-18')

searching = Search()
searching.purchase(custumers,'2025-07-12')