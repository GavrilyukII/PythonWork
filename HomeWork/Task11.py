# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int (input ('Введите число: '))
def arrayDigit (n):
    list = []
    for i in range (1,n+1):
        list.append((1+1/i)**i)
    return list
print(arrayDigit(n))
print(sum(arrayDigit(n)))