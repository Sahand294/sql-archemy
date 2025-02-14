import  json
with open('user_info.json','r',encoding='utf-8') as text:
    json1 = json.load(text)
json1['users'][1]['email'] = "sara123@example.com"
with open('user_info.json','w') as file:
    json.dump(json1,file,indent=2)
