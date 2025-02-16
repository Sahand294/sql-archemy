from  projects.exercises.prostgresssql.total import DataBase
import json
class Check:
    @staticmethod
    def checkd(title,author):
        r = DataBase.read(f"digital_book")
        error = False
        for i in r:
            if i['title'] == title and i['author'] == author:
                error = True
        return error
    @staticmethod
    def checkj(title,author):
        with open('idk.json','r',encoding='utf-8') as text1:
            json3 = json.load(text1)
        error = False
        for i in json3['books']:
            if i['title'] == title and i['author'] == author:
                error = True
        return error