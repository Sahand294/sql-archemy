# 1:json object and json arrey
# 2:{key,value},[{key,value},...]
import json

data = {"name": "sahand", "age": 10}
json_str = json.dumps(data)
#print(json_str)
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
json1 = '''
{
    "name": "John",
    "age": 30,
    "isStudent": false,
    "courses": ["Math", "Science"],
    "address": {
        "city": "New York",
        "zipcode": "10001"
    }
}
'''
json2 = json.loads(json1)
# print(json2['address']['city'])
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!111
with open('test.json','r',encoding='utf-8') as text1:
    json3 = json.load(text1)
for x,i in enumerate(json3['professors']):
    if i['id'] == 1:
        pass
        #print(i)
print(json3)
json3['professors'].append({'id':9999})
print(json3)
#print('{"professors": [{"id": 1,"name": "Dr. Ali Rezaei","department": "Computer Science","email": "ali.rezaei@university.edu","years_of_experience": 15,"courses": ["Data Structures","Algorithms","Database Systems"},{"id": 2,"name": "Prof. Sara Mohammadi","department": "Electrical Engineering","email": "sara.mohammadi@university.edu","years_of_experience": 20,"courses": ["Circuit Theory","Electromagnetics","Control Systems"]},{"id": 3,"name": "Dr. Mohammad Jafari","department": "Mechanical Engineering","email": "mohammad.jafari@university.edu","years_of_experience": 10,"courses": ["Thermodynamics","Fluid Mechanics","Dynamics"]]]}'*999999999999999)
