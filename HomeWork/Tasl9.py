# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

n = (input('Введите вещественное число: '))
if float(n) < 0:
    n= float(n)* (-1)
sum = 0
for i in str(n):
    if i != '.':
        sum+=int(i)
print (sum)

