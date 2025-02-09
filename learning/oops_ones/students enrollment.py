class Student:
    def __init__(self):
        self.students = {}
    def review(self):
        return self.students
    def add_Students(self, name, id):
        if id in self.students:
            raise Exception('there is already a student like that')
        else:
            self.courses = []
            self.name = name
            self.id = id
            self.students[id] = {'name':name,'id':id,'studies':self.courses}
        print('succesfully added!')


    def addingcourse(self,student_id:int,course,courses):
            if course in courses:
                self.students[student_id]['studies'].append({'name':course})

            else:
                print(f'the course {course} is not present')
class Grades:
    def gradeadding(self,name:int,coursname,grade,base):
        for i,x in enumerate(base[name]['studies']):
            if base[name]['studies'][i]['name'] == coursname:
                base[name]['studies'][i][f'grade for {base[name]['studies'][i]['name']}'] = grade
            else:
                print('no such course')
class Courses:
    def __init__(self):
        self.lists = {}
    def addingcourse(self, name):
        if name in self.lists:
            raise Exception('there is already a course')
        else:
            self.lists[name] = {'name':name,'enrolled students':[]}
    def addingenrollments(self,subject,studentid):
        self.lists[subject]['enrolled students'].append(studentid)
students = Student()
subjects = Courses()
grades = Grades()
math = subjects.addingcourse('math')
science = subjects.addingcourse('science')

student1 = students.add_Students('sam',102)

students.addingcourse(102,'math',subjects.lists)


grades.gradeadding(102,'math',100,students.students)
subjects.addingenrollments('math','sam')
print(students.review())
