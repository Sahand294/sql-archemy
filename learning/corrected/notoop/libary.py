math = ["Flatland", "Gödel,Escher,Bach"]
science = ["A Brief History of Time", "The Selfish Gene"]
fairytale = ["Grimm's Fairy Tales", "The Blue Fairy Book"]
borrowed = 0
hey = True
while hey:
    if borrowed == 0:
        catagory = input('would you like to borrow a book  or view catagorys or exit:')
        if catagory == 'exit':
            exit()
        elif catagory == 'view':
            cat = input(' from math science and fiarytale what catagory:')
            if cat == 'math':
                print(math)
            elif cat == 'science':
                print(science)
            elif cat == 'fairytale':
                print(fairytale)
        elif catagory == 'borrow':
            cato = input('from what catogory:')
            if cato == 'math':
                book = input(f'out of these books {math} which one:')
                math.remove(book)
                borrowed = 1
            elif cato == 'science':
                book = input(f'out of these books {science} which one:')
                science.remove(book)
                borrowed = 1
            elif cato == 'fairytale':
                book = input(f'out of these books {fairytale} which one:')
                fairytale.remove(book)
                borrowed = 1
    if borrowed == 1:
        catagory = input('would you like to return the books you have or view catagorys or exit:')
        if catagory == 'exit':
            exit()
        elif catagory == 'view':
            cat = input('what catagory:')
            if cat == 'math':
                print(math)
            elif cat == 'science':
                print(science)
            elif cat == 'fairytale':
                print(fairytale)
        if catagory == 'return':
            cato = input('what was the catogory:')
            if cato == 'math':
                math.append(book)
                borrowed = 0
            elif cato == 'science':
                science.append(book)
                borrowed = 0
            elif cato == 'fairytale':
                fairytale.append(book)
                borrowed = 0