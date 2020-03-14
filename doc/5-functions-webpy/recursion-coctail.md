# Рекурсивный коктейль.

Состоит из 30% воды 20% спирта и 50% рекурсивного коктеля :-).

    print("Making recousion coctail!!!")

    def make(water,alcohol):
        mix = 0
        mix = mix + (water*30)
        mix = mix + (alcohol*20)
        mix = mix + (make(water,alcohol)*50)
        return mix
        
    print(make(4,5))    
    
>>> RuntimeError: maximum recursion depth exceeded

Добавим счетчик итерации и ограничим рекурсию.

    def make(water,alcohol,cnt):
        cnt += 1
        mix = 0
        mix = mix + (water*30)
        mix = mix + (alcohol*20)
        if cnt >10:
            return mix
        mix = mix + (make(water,alcohol,cnt)*50)
        return mix

    cnt = 0    
    print(make(4,5,cnt))
