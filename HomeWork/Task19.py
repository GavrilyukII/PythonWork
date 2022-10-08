# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
import math 

n = int(input('Введите натуральное число: '))
mylist = []

def multiplierNumber(n): 
    while n % 2 == 0: 
        mylist.append(2) 
        n = n / 2 
 
    for i in range(3, int(math.sqrt(n)) + 1, 2): 
 
        while n % i == 0: 
            mylist.append(i) 
            n = n / i 
    if n > 2: 
        mylist.append(n) 
 
multiplierNumber(n) 
print(mylist)