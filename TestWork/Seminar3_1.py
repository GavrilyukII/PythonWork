
mylist = ['13kdjfh','kdjf','764hfjf','dhdfh','kdjf']
n = input("Введите искомое значение: ")
trigger = False
for i in range (len(mylist)):
    if mylist[i].find(n) >=0:
        trigger = True
        break
if trigger:
    print ('Значение присутствует')
else:
    print ('Значение отсутствует')