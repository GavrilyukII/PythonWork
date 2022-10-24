import model 

def PrintPhoneBook ():                           #Выводим строки из списка в консоль
    for i, item in enumerate(model.phonebook):
        print (i, item)

def MainMenu ():
    print ('\nГлавное меню:')
    print ('1. Добавить контакт')
    print ('2. Удалить контакт')
    print ('3. Изменить контакт')
    print ('4. Найти контакт')
    print ('8. Сохраниить')
    print ('0. Выйти')