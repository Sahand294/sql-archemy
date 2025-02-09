from students import Student as student
Student = student
class Grades:
    def add_grades(self, subject, grade,student):
        if not isinstance(student,Student):
            raise ValueError('no such student')
        if subject not in student.subjects:
            raise KeyError('no such subject!')
        student.subjects[subject] = grade

    def GPA(self,student):
        if not isinstance(student,Student):
            raise ValueError('no such student')
        A = 4
        B = 3
        C = 2
        D = 1
        F = 0
        gpa = 0
        number_of_subjects = -1
        n = 1
        for i in student.subjects:
            number_of_subjects += 1
            if n == 1:
                n = 0
            else:
                if student.subjects[i] >= 90:
                    gpa += A
                elif 80 <= student.subjects[i] < 90:
                    gpa += B
                elif 70 <= student.subjects[i] < 80:
                    gpa += C
                elif 60 <= student.subjects[i] < 70:
                    gpa += D
                elif 0 <= student.subjects[i] < 60:
                    gpa += F

        gpas1 = gpa / number_of_subjects
        gpas2 = gpas1 / 4.0
        student.subjects['gpa'] = gpas2*100
