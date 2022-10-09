# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

Eq1 = r'PythonWork/HomeWork/TextTask22_1.txt'
Eq2 = r'PythonWork/HomeWork/TextTask22_2.txt'

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

print (file1)
print (file2)

