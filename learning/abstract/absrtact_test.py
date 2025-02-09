from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self,r):
        self.r = r
    def area(self):
        return ((self.r * self.r) * 3.14)

    def perimeter(self):
        pass
c = Circle(10)
print(c.area())