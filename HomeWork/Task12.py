# Реализуйте алгоритм перемешивания списка.

from random import shuffle


n = int (input ("Введите размер списка: "))

list = []
for i in range (n):
    list.append(i)

print (list)

shuffle(list)

print (list)

