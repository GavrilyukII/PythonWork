# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

from operator import eq


Eq1 = r'PythonWork/HomeWork/TextTask22_1.txt'
Eq2 = r'PythonWork/HomeWork/TextTask22_2.txt'
Eq3 = r'PythonWork/HomeWork/TextTask22_3.txt'
equation1 = {}
equation2 = {}
try:
    with open (Eq1) as data:
        file1 = data.read()
except:
    print ("Ошибка данных")

try:
    with open (Eq2) as data:
        file2 = data.read()
except:
    print ("Ошибка данных")

file1 = file1.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]
file2 = file2.replace(' + ', ' +').replace(' - ', ' -').split()[:-2]

for i in range (len(file1)):
    file1[i] = file1[i].replace('+', '').split('x**')
    equation1[int(file1[i][1])] = int(file1[i][0])

for i in range (len(file2)):
    file2[i] = file2[i].replace('+', '').split('x**')
    equation2[int(file2[i][1])] = int(file2[i][0])

print (file1)
print (equation1)
print (file2)
print (equation2)

resultEquation = {}

for i in range (max(len(equation1),len(equation2))-1, -1, -1):
    first = equation1.get(i)
    second = equation2.get(i)
    if first != None or second != None:
        resultEquation[i] = (first if first != None else 0) + (second if second != None else 0)
print (resultEquation)

finalfile = ''
for i in range (len(resultEquation)-1, -1, -1):
        finalfile += f'{resultEquation.get(i)}*x**{i} + '


finalfile = finalfile.replace('x**1', 'x').replace('*x**0', '').replace('+ -', '- ')[:-2] + '= 0'
print(finalfile[:-3] + ' = 0')

try:
    with open (Eq3, 'w') as data:
        data.write(finalfile)
except:
    print("Ошибка обработки файла")