## Определение словаря

    mydict = {"one": 1 "two": 2}
    print(mydict)
    
## Получение элемента по ключу.

    mydict['one']
    
## Добавление пар ключ-значение.

    mydict['three'] = 3
    
## Удаление.

    del mydict['one']
    
## Вложенный список в словаре.

    lst = range(5)
    mydict['lst'] = lst
    
## Цикл по парам словаря.

    for v in mydict:
        print v
        
    for k,v in mydict.iteritems():
       print k
       print v    
       
## Изменение словарей.

     mydict = otherdict
     mydict['add'] = 2
     otherdict['add'] # выдаст 2      
     
При присваивании создается ссылка на одно и то же место в памяти.
Чтобы клонировать словарь в новую переменную необходимо использовать функцию copy().

    new = mydict.copy()
