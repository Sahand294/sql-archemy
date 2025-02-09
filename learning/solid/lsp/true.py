class Bird:
    def sound(self):
        pass
    def eating(self):
        pass
class BirdsThatCANFLY(Bird):
    def flying(self):
        pass
class BirdsThatCantFly(Bird):
    def walking(self):
        pass
    def sliding(self):
        pass
    def gliding(self):
        pass
class Penguin(BirdsThatCantFly):
    pass