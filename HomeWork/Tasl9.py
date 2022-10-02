# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# 0,56 -> 11

# Вариант 1 (моё решение)
n = (input('Введите вещественное число: '))
if float(n) < 0:
    n= float(n)* (-1)
sum = 0
for i in str(n):
    if i != '.':
        sum+=int(i)
print (f"{n} -> {sum}")

# Вариант 2 (семинар)
# number = input ('Введите вещественное число: ')
# summa = 0
# for i in number:
#     if i.isdigit():
#         summa+=int(i)
# print (summa)

# Вариант 3 (семинар)
# number = float(input('Введите вещественное число: '))
# summa = 0
# while int(number) != number:
#     number*=10
# print (number)

# while number !=0:
#     summa+=number%10
#     number//=10
# print (summa)