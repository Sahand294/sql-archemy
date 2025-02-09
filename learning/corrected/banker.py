from datetime import datetime

heyeyyey = []
lg = []


class Info:
    def __init__(self, year, month, day, data, type, amount):
        self.type = type
        self.amount = amount
        wassup = datetime(year, month, day)
        wassup1 = wassup.strftime("%B %d, %Y")
        data.append(f'{wassup1}:{type} ${amount}')
        self.realdate = datetime(year, month, day)


class DateTracker:
    def year(self, year, lists):
        for i, x in enumerate(lists):
            if x.realdate.year == year:
                print(lg[i])

    def month(self, month, lists):
        for i,x in enumerate(lists):
            if x.realdate.month == month:
                print(i)

    def both(self, year, month, lists):
        for i,x  in enumerate(lists):
            if x.realdate.year == year:
                if x.realdate.month == month:
                    print(i)





hey = Info(2024, 11, 1, lg, 'deposit', 1000)
he = Info(2023, 5, 10, lg, 'deposit', 1000)
heyeyyey.append(hey)
heyeyyey.append(he)
dater = DateTracker()
dater.year(2023,heyeyyey)