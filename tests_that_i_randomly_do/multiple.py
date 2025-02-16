num = float(input('m:'))
num1 = float(input('1:'))
num2 = float(input('2:'))
y = 0
e = True
while e:
    if num1 == num2:
        e = False
    else:
        num1 += num
        t = num + num1
        y += t
print(y)
