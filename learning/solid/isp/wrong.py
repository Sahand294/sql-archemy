from abc import abstractmethod,ABC
class Print:
    @abstractmethod
    def document(self):
        pass

    @abstractmethod
    def scaning(self):
        pass

    @abstractmethod
    def inksupply(self):
        pass
class Multiprinter(Print):
    def inksupply(self):
        pass

    def scaning(self):
        pass

    def document(self):
        pass


class SimplePrinter(Print):
    def inksupply(self):
        pass

    def scaning(self):
        raise NotImplementedError("SIMPLE PRINTER IS TOO SIMPLE")

    def document(self):
        pass