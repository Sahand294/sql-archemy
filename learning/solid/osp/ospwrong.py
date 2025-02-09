class Discount:
    def calculate(self,amounts,typediscount):
        if typediscount == "percentage":
            return amounts *0.1
        else:
            return amounts - 20

