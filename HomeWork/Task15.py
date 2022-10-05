# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# ВАЖНО: если число целое, то оно не имеет дробной части и засчитывать 0 как минимальное не стоит
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

n = int (input('Введите размер списка: '))
mylist = []
def fillArray (list):
    for i in range (n):
        list.append(round(random.uniform(1,100),2))
    return list 

fillArray (mylist)
print(mylist)

# Вначале решил для max и min элементов списка (не дробной части), поэтому результат может быть отрицательным (p.s. ВНИМАТЕЛЬНО ЧИТАЙ УСЛОВИЕ)
# max = 0
# min = 100
# for i in mylist:
#     if i>=max:
#         max=i
#     if i<=min:
#         min=i
# print (max,min)

# print (round((round(float(max%1),2)) - (round(float(min%1),2)),2))

min = 1
max = 0
for i in mylist:
    if (i - int(i)) <= min:
        min = i - int(i)
    if (i - int(i)) >= max:
        max = i - int(i)  
print(round((max),2),round((min),2))
print(round((max-min),2))
