# Задайте рандомно список из чисел размером N, где N число с клавиатуры. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

n = int (input('Введите размер списка: '))
mylist = []
def fillArray (list):
    for i in range (n):
        list.append(randint(1,100))
    return list

fillArray (mylist)
print(mylist)
sum = 0
for i in range (len(mylist)):
    if i%2!=0:
        sum = sum + mylist[i]
print (sum)