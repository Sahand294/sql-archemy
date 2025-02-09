from subjects import Subjects as subjects
from grade_handeling import  Grades as grades
from students import Student
Grades = grades()
Subjects = subjects()







sahand = Student('sahand', 5949)
Subjects.add_subjects('math',sahand)
Subjects.add_subjects('physics',sahand)

Grades.add_grades('math', 96,sahand)
Grades.add_grades('physics', 85,sahand)
Grades.GPA(sahand)
print(sahand.show())
