# Определить позицию второго вхождения строки в списке, либо сообщение что не найдено
# Пример:
# Список - ['qwekrjt','jdhfh','hdhqwek','qwe','hjdfjhdf'], ищем 'qwe', ответ = 3

mylist = ['qwe','hfdj','qwe','dje3j4','jd33','hfdj','jd33']
n = str(input('Введите строку для поиска: '))
count = 0
for i in range(len(mylist)):
    if n in mylist[i]:
        count+=1
        if count == 2:
            print (i)
            break
else:
    print('Не найдено')
