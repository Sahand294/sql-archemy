import json
with open('usernames.json','r',encoding='utf-8') as file:
    json1 = json.load(file)
invalid_user_names = []
nums_and_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','1','2','3','4','5','6','7','8','9']
for i in json1['users']:
    for x in i['username']:
        if x not in nums_and_letters:
            invalid_user_names.append(i)
print(invalid_user_names)