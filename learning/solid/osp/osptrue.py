from abc import abstractmethod


class Discount:
    @abstractmethod
    def calculate(self, amounts):
        pass
    def clouds(self):
        pass


class PercentageDiscount(Discount):
    def calculate(self, amounts):
        return amounts * 0.1
