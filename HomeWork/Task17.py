# Задайте число - размер списка. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]


n = int(input('Введите размер: '))

def getfibonacci(n):
    fibList = []
    a = b = 1
    for i in range(1,n+1):
        fibList.append(a)
        a, b = b, a + b
    a, b = 0, 1
    for i in range (n+1):
        fibList.insert(0, a)
        a, b = b, a - b
    return fibList

fibList = getfibonacci(n)
print(getfibonacci(n))

# Без отрицательных индексов
# n = int (input('Введите размер: '))

# a = b = 1
  
# print(a, b, end=' ')
 
# for i in range(2, n):
#     a, b = b, a + b
#     print(b, end=' ')