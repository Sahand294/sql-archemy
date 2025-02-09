def hey():
    try:
        num1 = float(input('put a number:'))
        num2 = float(input('put a number:'))
        num3 = num1 / num2
    except ValueError:
        print('value error')
    except ZeroDivisionError:
        print('division error')

    else:
        print(num3)
    finally:
        print('done')
hey()