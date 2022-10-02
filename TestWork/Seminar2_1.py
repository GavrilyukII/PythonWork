# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# Пример: Для N = 5: 1, -3, 9, -27, 81

# Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Пример: Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int (input ('Введите натуральное число: '))
list=[]
for i in range (n):
    list.append(f"{i} : {3*i+1}")
print (list)

# n = int(input('введите число: '))
# list = []
# for i in range(1, n + 1):
#     list.append(f"{i} : {3 * i + 1}")
# print(", ".join(list))

# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# str1=str(input())
# str2=str(input())

# count = 0
# for i in range (str1):
#     for j in range (str2):
#         if (i == j):
#             count += 1
# print (count)  

# textFirst = input('Введите первую строку: ')
# textSecond = input('Введите вторую строку: ')



# string = ''
# subString = ''


# if len(textFirst) > len(textSecond):
#     string = textFirst
#     subString = textSecond
# else:
#     string = textSecond
#     subString = textFirst


# print(string.count(subString))

stringFirst = input("Введите первую строку: ")
stringSecond = input("Введите вторую строку: ")

source = ''
subString = ''
count = 0

if len(stringFirst) > len(stringSecond):
    source = stringFirst
    subString = stringSecond
else:
    source = stringSecond
    subString = stringFirst

for i in range(len(source)):
    temp = source[i:i+len(subString)]
    if temp == subString:
        count += 1

print(f'В строке "{source}" подстрока "{subString}" встречается {count} раз')

