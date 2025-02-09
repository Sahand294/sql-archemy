class Student:
    def __init__(self, name: str, id):
        self.subjects = {'gpa': 0}
        self.name = name
        self.id = id
    def show(self):
        return self.subjects