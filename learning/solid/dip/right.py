from abc import ABC, abstractmethod


class WorkerInterFace:
    @abstractmethod
    def working(self):
        pass


class Worker(WorkerInterFace):

    def working(self):
        pass
class Manager:
    def __init__(self,worker:WorkerInterFace):
        self.workers = worker
    def manage(self):
        self.workers.working()
#instead of the original classes use the parts in other classes we copy it
#so if someone new comes we don't have to change the manager and every time she uss working interface she tells everyone
