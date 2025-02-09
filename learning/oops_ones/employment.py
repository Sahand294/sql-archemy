class Info:
    def __init__(self,name,id,job):
        self.name = name
        self.id = id
        self.job = job
class TypeSalary:
    def __init__(self,information):
        info = information
        if info.job == 'dev':
            Salary('dev',info.id,info.name)
        if info.job == 'manager':
            Salary('manager',info.id,info.name)
        if info.job == 'manager_dev':
            Salary('manager_dev',info.id,info.name)
class Salary:
    def __init__(self,job,id,name):
        if job == 'dev':
            print(f'{id}  {name} has just earned 1000$')
        elif job == 'manager':
            print(f'{id}  {name} has just earned 3000$')
        elif job == 'manager_dev':
            print(f'{id}  {name} has just earned 10000$')
sahand = Info('sahand',18375,'manager_dev')
javad = Info('javad',1756,'dev')
hassan = Info('hassan',62973,'manager')
workers = [sahand,javad,hassan]
class GivingSalary:
    def __init__(self):
        for i in workers:
            TypeSalary(i)
GivingSalary()