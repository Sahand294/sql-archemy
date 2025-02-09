class Bird:
    def flying(self):
        pass
    def music(self):
        pass
class Eagle(Bird):
    pass
class Penguin(Bird):
    def flying(self):
        raise NotImplementedError("penguins cant fly")