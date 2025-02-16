num1 = float(input('1:'))+1
num2 = float(input('2:'))+1
t = 0
e = True
while e:
    num1 += 2
    if num1 > num2:
        e = False
    else:
        t += num1
print(t)