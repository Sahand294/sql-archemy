import json
class Adding_book:
    @staticmethod
    def json(title,author,publication_year):
        with open('idk.json', 'r', encoding='utf-8') as text:
            dot = json.load(text)
        dot['books'].append({'title':title,'author':author,'publication year':publication_year})
        with open('idk.json', 'w') as file:
            json.dump(dot,file,indent=3)
    @staticmethod
    def database():
        pass