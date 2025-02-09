import json
from datetime import datetime
date = datetime.now()
time = date.strftime('date %y:%b:%d time %H:%M:%S')
with open('the_tests_compare.json', 'r', encoding='utf-8') as text2:
    json2 = json.load(text2)
with open('test.json', 'r', encoding='utf-8') as text1:
    json1 = json.load(text1)


class Comparsion:
    @staticmethod
    def id(example_1, example_2):
        num1 = False
        num2 = False
        iddata1 = []
        iddata2 = []
        for x, i in enumerate(example_1['users']):
            iddata1.append(i['id'])
        for x, i in enumerate(example_2['users']):
            iddata2.append(i['id'])
        if iddata1[0] == iddata2[0]:
            num1 = True
        else:
            num1 = False
        if iddata1[1] == iddata2[1]:
            num2 = True
        else:
            num2 = False
        if not num1:
            first_user = f'changed to {iddata1[0]}'
        else:
            first_user = 'stable'
        if not num2:
            second_user = f'changed to {iddata1[1]}'
        else:
            second_user = 'stable'
        return [first_user, second_user, iddata2[0], iddata2[1]]

    @staticmethod
    def name(example_1, example_2):
        num1 = False
        num2 = False
        iddata1 = []
        iddata2 = []
        for x, i in enumerate(example_1['users']):
            iddata1.append(i['name'])
        for x, i in enumerate(example_2['users']):
            iddata2.append(i['name'])
        if iddata1[0] == iddata2[0]:
            num1 = True
        else:
            num1 = False
        if iddata1[1] == iddata2[1]:
            num2 = True
        else:
            num2 = False
        if not num1:
            first_user = f'changed to {iddata1[0]}'
        else:
            first_user = 'stable'
        if not num2:
            second_user = f'changed to {iddata1[1]}'
        else:
            second_user = 'stable'
        return [first_user, second_user, iddata2[0], iddata2[1]]

    @staticmethod
    def email(example_1, example_2):
        num1 = False
        num2 = False
        iddata1 = []
        iddata2 = []
        for x, i in enumerate(example_1['users']):
            iddata1.append(i['email'])
        for x, i in enumerate(example_2['users']):
            iddata2.append(i['email'])
        if iddata1[0] == iddata2[0]:
            num1 = True
        else:
            num1 = False
        if iddata1[1] == iddata2[1]:
            num2 = True
        else:
            num2 = False
        if not num1:
            first_user = f'changed to {iddata1[0]}'
        else:
            first_user = 'stable'
        if not num2:
            second_user = f'changed to {iddata1[1]}'
        else:
            second_user = 'stable'
        return [first_user, second_user, iddata2[0], iddata2[1]]

    @staticmethod
    def age(example_1, example_2):
        num1 = False
        num2 = False
        iddata1 = []
        iddata2 = []
        for x, i in enumerate(example_1['users']):
            iddata1.append(i['age'])
        for x, i in enumerate(example_2['users']):
            iddata2.append(i['age'])
        if iddata1[0] == iddata2[0]:
            num1 = True
        else:
            num1 = False
        if iddata1[1] == iddata2[1]:
            num2 = True
        else:
            num2 = False
        if not num1:
            first_user = f'changed to {iddata1[0]}'
        else:
            first_user = 'stable'
        if not num2:
            second_user = f'changed to {iddata1[1]}'
        else:
            second_user = 'stable'
        return [first_user, second_user, iddata2[0], iddata2[1]]


class changing_history:
    def __init__(self, file, new_file,the_comparsion_file):
        with open(file, 'w') as text3:
            json.dump(new_file,text3,indent=4)
        self.changing_the_comparsion(the_comparsion_file,new_file)
    def changing_the_comparsion(self,files_name,new_file):
        with open('the_tests_compare.json','w') as texx:

            json.dump(new_file,texx,indent=4)



class history_writing:
    @staticmethod
    def id():
        first_id_status, second_id_status, old_first_id, old_second_id = Comparsion.id(json1, json2)
        if first_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'id:{old_first_id} to {first_id_status} at {time}')
        if second_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'id:{old_second_id} to {second_id_status} at {time}')
        changing_history('test.json',json1,'the_tests_compare.json')

    @staticmethod
    def name():
        first_id_status, second_id_status, old_first_id, old_second_id = Comparsion.name(json1, json2)
        if first_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'name:{old_first_id} to {first_id_status} at {time}')
        if second_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'name:{old_second_id} to {second_id_status} at {time}')
        changing_history('test.json', json1,'the_tests_compare.json')

    @staticmethod
    def email():
        first_id_status, second_id_status, old_first_id, old_second_id = Comparsion.email(json1, json2)
        if first_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'email:{old_first_id} to {first_id_status} at {time}')
        if second_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'email:{old_second_id} to {second_id_status} at {time}')
        changing_history('test.json',json1,'the_tests_compare.json')

    @staticmethod
    def age():
        first_id_status, second_id_status, old_first_id, old_second_id = Comparsion.age(json1, json2)
        if first_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'age:{old_first_id} to {first_id_status} at {time}')
        if second_id_status == 'stable':
            pass
        else:
            json1['history'].append(f'age:{old_second_id} to {second_id_status} at {time}')
        changing_history('test.json',json1,'the_tests_compare.json')
class doing:
    @staticmethod
    def doing_all():
        history_writing.id()
        history_writing.email()
        history_writing.name()
        history_writing.age()
d = doing()
d.doing_all()