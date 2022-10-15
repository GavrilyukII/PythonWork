# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

# mylist = ['1113384455229']
# mylist2 = []
# for i in mylist:
#     for j in list(i):
#         mylist2.append(j)
# print(mylist2)
# newMylist = dict((i, mylist2.count(i)) for i in mylist2)
# print (newMylist)

# listfinal = []
# def get_key(newMylist, value):
#     for k, v in newMylist.items():
#         if v == value:
#             listfinal.append(k)
# get_key(newMylist, 1)
# print (listfinal)

# Ну это был ад конечно, через словарь

lst = list(map(int, input("Введите числа через пробел:\n").split()))
print(f"Исходный список: {lst}")
new_lst = []
[new_lst.append(i) for i in lst if i not in new_lst]
print(f"Список из неповторяющихся элементов: {new_lst}")