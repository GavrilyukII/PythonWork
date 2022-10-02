# Реализуйте алгоритм перемешивания списка.

# from random import shuffle
# n = int (input ("Введите размер списка: "))
# list = []
# for i in range (n):
#     list.append(i)
# print (list)
# shuffle(list)
# print (list)

import random

list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print (list)
listA = []
for i in range (0, len(list)):
    j = random.randrange(0, len(list))
    listA.append(list[j])
    list.remove(list[j])
print(listA)
