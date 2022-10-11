# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python

import math


pathRead = r'PythonWork/TestWork/text1.txt'
pathWrite = r'PythonWork/TestWork/text2.txt'

try:
    with open (pathRead) as data:
        file = data.read().split(' ')
except:
    print ("Ошибка данных")

print (file)

mylist = []

for elem in file:
    if elem[0].isdigit():
        mylist.append(elem[0])
print (mylist)

a = int(mylist[0])
b = int(mylist[1])
c = int(mylist[2])
print(a,b,c)

result = ''

discr = b**2 - 4*a*c
print (discr)
if discr > 0:
    x1 = (-b + math.sqrt(discr)) / (2*a)
    x2 = (-b + math.sqrt(discr)) / (2*a)
    result = f'x1 = {x1}\n x2 = {x2}'
elif discr == 0:
    x = -b / (2*a)
    result = f'x1=x2={x}'
else:
    print ('Корней нет')

try:
    with open (pathWrite, 'w') as data:
        data.write(result)
except:
    print("Ошибка работы с файлом")