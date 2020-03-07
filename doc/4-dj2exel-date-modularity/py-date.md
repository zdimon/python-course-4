## Работа с датой.

Текущая дата.

    import datetime
    from time import strftime
    print("Current date")
    print(datetime.datetime.now())
    print(datetime.datetime.now().time())
    
### Форматирование даты.

    now = datetime.datetime.now()
    now.strftime("%Y-%m-%d %H:%M")
    
### Прибавление к дате дней.

    from datetime import timedelta
    d = now - timedelta(days=6)
    
### timedelta()

    datetime.timedelta(microseconds=1)
    datetime.timedelta(milliseconds=1)
    datetime.timedelta(seconds=1)
    datetime.timedelta(minutes=1)
    datetime.timedelta(hours=1)
    datetime.timedelta(days=1)
    datetime.timedelta(weeks=1)

    
    
### Прибавление месяцев (модуль dateutil).

    from dateutil.relativedelta import relativedelta
    date_after_month = datetime.datetime.today() + relativedelta(months=1)
    print ('Today: %s' % datetime.datetime.today().strftime('%d/%m/%Y'))
    print ('After Month: %s' % date_after_month.strftime('%d/%m/%Y'))
    
### Атрибуты объекта даты.

    import datetime
    today = datetime.date.today()
    print ('Year: %s' % today.year)
    print ('Mon : %s' % today.month)
    print ('Day : %s' % today.day)
    
    
### Замена параметров даты.

    print(date_after_month.replace(year=2000))

### Сравнение 


    t1 = datetime.time(14, 55, 0)
    t2 = datetime.time(13,56,0)
    print(t1<t2)




    
