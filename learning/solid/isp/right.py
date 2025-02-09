from abc import ABC,abstractmethod
class PrintingOnly:
    @abstractmethod
    def printing(self):
        pass
class Fax:
    @abstractmethod
    def faxinggocuments(self):
        pass

class multiprinter(PrintingOnly,Fax):
    def printing(self):
        pass

    def faxinggocuments(self):
        pass


class simpleprinter(PrintingOnly):
    def printing(self):
        pass