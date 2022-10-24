import model
import view

def start():
    read_phone_book()
    view.PrintPhoneBook()
    MainMenu()

def read_phone_book():
    with open(model.path, 'r', encoding = 'UTF-8') as data:
        contacts_list = data.read().split('\n')
        model.phonebook = contacts_list

def save_file():
        with open(model.path, 'w', encoding = 'UTF-8') as data:
            data.write('\n'.join(model.phonebook))

def MainMenu ():
    while True:
        view.MainMenu ()
        choice = int(input('\nВыберите пункт: '))
        match(choice):
            case 1: 
                add_contact()
                print ('Контакт добавлен')
            case 2: 
                delete_contact()
                print ('Контакт удален')
            case 3:
                change_contact()
                print ('Контакт изменен')
            case 4:
                pass
                found_contact()
            case 5:
                save_file()
                print ('Изменения сохранены')
            case 0:
                break

def add_contact():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    patronymic = input('Введите отчество: ')
    phone = input('Введите номер телефона: ')
    contacts = f'{surname}; {name}; {patronymic}; {phone};'
    model.phonebook.append(contacts)                         #Добавляем контакт с помощью append
    view.PrintPhoneBook()

def delete_contact():
    choice = int(input('Введите порядковый номер контакта для удаления: '))
    model.phonebook.pop(choice)                                #Удаляем (pop выдергивает) контакт с помощью pop
    view.PrintPhoneBook()

def change_contact():
    choice = int(input('Введите порядковый номер контакта для изменения: '))
    choice2 = int(input('Введите номер атрибута для изменения (0 - Фамилия, 1 - Имя, 2 - Отчетсво, 3 - Номер телефона): '))
    contact = model.phonebook.pop(choice).split(';')                #Присваиваем списку значение выбранного контакта (строки) с помощью выдергивания pop и разбиваем через ;
    contact[choice2] = input()                                  #Теперь присваиваем выбранному значению (атрибуту записанному в choice2) введенные с консоли данные
    model.phonebook.insert(choice, ';'.join(contact))           #Склеиваем обратно в выбранную строку значение переменной contact c учетом изменения
    view.PrintPhoneBook()

def found_contact():
    found = input('Введите искомое значение:')
    for line in model.phonebook:
        if found.lower() in line.lower():
            flag = 0
            print(f'\n{line}')
    if flag: print('\nКонтакт не найден')


#     # found = int(input('Введите номер атрибута для поиска (0 - Фамилия, 1 - Имя, 2 - Отчетсво, 3 - Номер телефона): '))
#     Found = input('Введите искомое значение: ')
#     for i in model.phonebook:
#         if model.phonebook[i].find(Found):
#             model.reslist.append(model.phonebook[i]).split(',')
# while True:
#     selector = choice()
#     if selector == 1:
#         query = ((input('Для поиска контакта введите его фамилию: ').capitalize(),
#                   input('Для поиска контакта введите его имя: ').capitalize()))
#         print(c.find_member(query))

# def read_phone_book ():
#     data = open('PythonWork/HomeWork/Telephone/phone_book.txt', 'r', encoding="UTF-8")
#     contacts_list = data.read().split('\n')
#     data.close()
#     model.phonebook = contacts_list

# phonebook=[]

# for i in file:
#     phonebook.append(i.replace(' ', '').split(';'))

# print(phonebook)

# dict = {}

# dict['Фамилия'] = phonebook [0][0]
# dict['Имя'] = phonebook [0][1]
# dict['Отчество'] = phonebook [0][2]
# dict['Телефон'] = phonebook [0][3]

# print(dict)
