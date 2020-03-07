## Домашнее задание.


## Переписать на функциях.

### Функции колоды

- создание перемешанной колоды

- доставание карты

## Функции игры

- инициализация (создание колоды и словаря статистики с очками для бота и игрока и выиграшем) 

- делание ставки игроком

- игра бота

- старт игры

- конец игры

## Переписать на классах.

- класс колоды

- класс бота

- класс игрока

- класс игры

Пример.

    koloda = [6,7,8,9,10,2,3,4,11] * 4

    import random
    from termcolor import colored

    random.shuffle(koloda)


    print('Поиграем в очко?')
    count = 0
    botcount = 0

    while True:
        choice = input('Будете брать карту? y/n\n')
        if choice == 'y':
            current = koloda.pop()
            bot = koloda.pop()
            print(colored('Вам попалась карта достоинством %d' %current, 'red'))
            print(colored('Боту попалось карта достоинством %d' %bot, "blue"))
            count += current
            botcount += bot
            if count > 21:
                print('Извините, но вы проиграли')
                break
            elif count == 21:
                print('Поздравляю, вы набрали 21!')
                print("Бот набрал %d" %botcount)
                break
            elif botcount == 21:
                print("Бот набрал %d" %botcount )
                break
            elif botcount > 21:
                print("Бот проиграл")
                print("Ты набрал %d" %count)
                break
            else:
                print("-----------------------------------")
                print(colored('У вас %d очков.' %count, "red"))
                print(colored('У бота %d очков.' %botcount, "blue"))
        elif choice == 'n':
            print('У вас %d очков и вы закончили игру.' %count)
            print('У бота %d очков и вы закончили игру.' %botcount)
            break
          


    print('До новых встреч!')
