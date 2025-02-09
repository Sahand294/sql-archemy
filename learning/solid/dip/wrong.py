class Worker:
    def working(self):
        pass


class Manager:
    def __init__(self):
        self.worker = Worker()

    def manage(self):
        self.worker.working()
