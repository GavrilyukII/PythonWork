# Напишите программу, которая найдёт произведение пар чисел списка (CСписок создаем как в предыдущем задании). 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

from random import randint

n = int (input('Введите размер списка: '))
mylist = []
def fillArray (list):
    for i in range (n):
        list.append(randint(1,100))
    return list

fillArray (mylist)
print(mylist)

reslist = []
for i in range ((len(mylist)+1)//2):
    reslist.append(mylist[i]*mylist[len(mylist)-1-i])
print(reslist)

# разложил для себя, тупого
# 0   1   2   3   4   5   6 
# 60, 37, 89, 94, 67, 25, 100

# mylist[i] * mylist[len(mylist) -1 -i]
# 60 (0) * 100 (7 -1 -0 = 6)
# 37(1) * 25 (7-1-1=5)
# 89(2) * 67(7-1-2=4)
# 94(3) * 94(7-1-3=3) 
