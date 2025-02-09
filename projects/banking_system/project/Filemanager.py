import csv


class Filemanager:
    @staticmethod
    def checking_the_key(key):
        if key != 'balance':
            if key != 'password':
                if key != 'owner':
                    raise KeyError('no such key')
                else:
                    return True
            else:
                return True
        else:
            return True

    @staticmethod
    def check_status(file: str, id: int, key: str):
        Filemanager.checking_the_key(key)
        try:
            with (open(file, 'r', encoding="utf-8") as text1):
                pass
        except:
            raise Exception('no such file')
        with (open(file, 'r', encoding="utf-8") as text1):
            r = csv.DictReader(text1)
            data = []
            for i in r:
                file = {key: value.strip() for key, value in i.items()}
                data.append(file)
            errors = 1
            for i in data:
                if i["id"] == str(id):
                    balance = i[key]
                    errors = 0
            if errors == 1:
                raise ValueError('no such account')
            if key == 'balance':
                return float(balance)
            return balance

    @staticmethod
    def changing_it(key: str, csv_file: str, id: int, new_value: str):
        Filemanager.checking_the_key(key)
        try:
            with (open(csv_file, 'r', encoding="utf-8") as text1):
                pass
        except:
            raise Exception('no such file')
        with open(csv_file, 'r', encoding="utf-8") as file:
            r = csv.DictReader(file)
            data = []
            for i in r:
                files = {key: value.strip() for key, value in i.items()}
                data.append(files)
        errors = 1
        for x, i in enumerate(data):
            if i['id'] == str(id):
                errors = 0
                if key == 'balance':
                    data[x]['balance'] = float(data[x]['balance']) + float(new_value)
                else:
                    data[x][key] = new_value

        if errors == 1:
            raise ValueError('no such account')
        with open(csv_file, "w", encoding="utf-8", newline="") as text:
            file = data[0].keys()
            writer = csv.DictWriter(text, fieldnames=file)
            writer.writeheader()
            writer.writerows(data)
        if key == 'password':
            with open(f"transaction", 'a') as text:
                text.write(f'\n{id} has changed the password to {new_value}')
        elif key == 'owner':
            with open(f"transaction", 'a') as text:
                text.write(f'\n{id} has changed the owner name to {new_value}')
        elif key == 'balance':
            if float(new_value) > 0:
                with open(f"transaction", 'a') as text:
                    text.write(
                        f'\n{id} has deposited {float(new_value)}$  balance:{Filemanager.check_status(csv_file, id, 'balance')}')
            else:
                with open(f"transaction", 'a') as text:
                    text.write(
                        f'\n{id} has withdraw {float(new_value)}$  balance:{Filemanager.check_status(csv_file, id, 'balance')}')
