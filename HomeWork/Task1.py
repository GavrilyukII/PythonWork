#Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# Примеры:
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# n = int (input('Введите число n: '))
# # print (n, "->", end = ' ')
# # for i in range(-n,n+1):
# #     print(i, end = ', ')

n = int (input('Введите число n: '))
reslist = [n for n in range (-n,n+1)]
print (reslist)