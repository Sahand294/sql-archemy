stats = {'radman': {'id': 1575975,
                   'grade': {'math': 97, 'science': 98, 'social studies': 100}},
         'sahand': {'id': 4194648,
                    'grade': {'math': 100, 'science': 100, 'social studies': 99}},
         'sophia': {'id': 7394847,
                  'grade': {'math': 9, 'science': 12, 'social studies': 30}}}
#we are doing with 3 diffrent grades with same names
passes = []
class Info:
    def __init__(self,studentsstorage):
        self.information = studentsstorage

class AvarageCalculator:
    def __init__(self,grade1,grade2,grade3,name):
        sum = grade1+grade2+grade3
        avarage = sum/3
    #    thereavaragevariable = avarage
        FailOrPass(avarage,name)
class FailOrPass:
    def __init__(self, avarage, names):
        if avarage <= 50:
            name = f'{names}, with the grade of {avarage} has failed'
            passes.append(name)
        else:
            name = f'{names}, with the grade of {avarage} has passed'
            passes.append(name)
stat = Info(stats)
for i in stat.information:
    AvarageCalculator(stat.information[i]['grade']['math'],stat.information[i]['grade']['science'],stat.information[i]['grade']['social studies'],i)
for x in passes:
    print(x)
