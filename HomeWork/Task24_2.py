from random import randint

# человек Х бот (с "мозгами")
print ('Итак, начнем игру! Для начала прочтите правила:\n''На столе лежит 150 конфет.\n''Каждый ход вы по очереди будете брать от 1 до 28 конфет.\n''Проиграет тот, кто сделает ход последним, так как все конфеты в таком случае достаются игроку сделавшему ход предпоследним.\n' )
offer = input('Согласны сыграть? (да/нет): ')

if offer == 'да':
    def quantCandy (name):
        x = int(input(f'{name}, введите количество конфет от 1 до 28: '))
        while x < 1 or x > 28:
            x = int(input(f'\n{name}, Вы ошиблись, введите корректное количество конфет от 1 до 28: '))
        return x

    def printMotion (name, m, count, general):
        print (f'\n{name} сделал(а) свой ход и взял(а) {m} конфет(ы), теперь у него(неё) {count}, осталось всего {general}')
    
    def skynetBrain (general):
        m = randint(1,29)
        while general-m <= 28 and general > 29:
            m = randint(1,29)
        return m

    player1 = input('\nВведите имя первого игрока: ')
    player2 = 'Скайнет'
    general = 150
    flag = randint(0,2)

    if flag:
        print(f'\nПервым(ой) ходит {player1}')
    else:
        print(f'\nПервым(ой) ходит {player2}')
    count1 = 0
    count2 = 0

    while general > 28:
        if flag:
            m = quantCandy(player1)
            count1+=m
            general-=m
            flag = False
            printMotion (player1, m, count1, general)
        else:
            m = skynetBrain(general)
            count2+=m
            general-=m
            flag = True
            printMotion (player2, m, count2, general)
    if flag:
        print (f'{player1} ПОБЕДИЛ(А)! УРА!')
    else:
        print (f'{player2} ПОБЕДИЛ! Ты проиграл Коннор!')
else:
    print ('Ну ладно, до встречи! (((')