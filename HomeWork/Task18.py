# Вычислить число c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

# так разве не проще?
# num = float(input('Введите число: '))
# d = int(input('Введите точность округления числа '))
# print (round(num,d))

# Но можно и так
from math import pi
d = input('Введите число, обозначающее точность для Пи:  ')
def get_count(d):
    s = str(d)
    if '.' in s:
        return abs(s.find('.') - len(s)) - 1
    else:
        return 0
print (get_count(d))
print (f'При точности {d} число Пи равно {round(pi, get_count(d))}')