# Домашнее задание. Списки.

1. Используя генератор списков, создать список, заполненый квадратами целых чисел от 1 до 5.

2. Используя генератор списков, создать список, заполненый 10 случайными числами от 1 до 10, удалить из него повторяющиеся значения.

3. Считать имена файлов внутри текущего каталога и вывести их на экран в виде списка, отсортированного по алфавиту.

4. Дана строка 'user1:23:user2:45:user3:37'

Преобразовать ее в список.

    ['user1',23,'user2',45,'user3',37]

затем получившейся список превратить в следующие форматы списков

    [['user1',23],['user2',45],['user3',37]]
    
    [['user1','user2','user3'],['23','45','37']]
    
Вопрос что делает этот код?

    a = [input() for i in range(int(input()))]
    
    a = [1,2,3,4]
    b = a[:]
