## Кортежи
 
Это неизменяемая последовательность из неизменяемых объектов Python.

    tup1 = ('physics', 'chemistry', 1997, 2000)
    tup2 = (1, 2, 3, 4, 5 )
    tup3 = "a", "b", "c", "d

Кортеж, состоящий из одного элемента должен сожержать запятую.

    tup1 = (50,)


### Доступ к значениям кортежа.

    print tup1[0]
    print tup2[1:5]

Вы не можете изменить кортеж либо значения его элементов.
Вы можете только извлекать из него один или несколько значений, создавая новый кортеж.


    #!/usr/bin/python

    tup1 = (12, 34.56);
    tup2 = ('abc', 'xyz');

    # Following action is not valid for tuples
    # tup1[0] = 100;

    # So let's create a new tuple as follows
    tup3 = tup1 + tup2;
    print tup3

### Удаление элементов.

Невозможно.

Вы можете только удалить весь кортеж целиком.

    tup = ('physics', 'chemistry', 1997, 2000);
    del tup;

###Basic Tuples Operations

Tuples respond to the + and * operators much like strings.


len((1, 2, 3))	3	Length
(1, 2, 3) + (4, 5, 6)	(1, 2, 3, 4, 5, 6)	Concatenation
('Hi!',) * 4	('Hi!', 'Hi!', 'Hi!', 'Hi!')	Repetition
3 in (1, 2, 3)	True	Membership
for x in (1, 2, 3): print x,	1 2 3	Iteration


### Встроенные функции кортежей.
	
Сравнение двух кортежей.
	
    cmp(tuple1, tuple2)


Длинна.
	

    len(tuple)


Максимальное значение.

	
    max(tuple)


Минимальное значение.
	
    min(tuple)


Преобразование списка в кортеж.
	
    tuple(seq)


### Использование кортежа как ключа словаря.


    d = {(1, 1, 1) : 1}








