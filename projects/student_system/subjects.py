from  students import Student as students
Student = students
class Subjects:
    def add_subjects(self, subjects,student):
        if not isinstance(student,Student):
            raise ValueError('no such student!')
        student.subjects[subjects] = 0
