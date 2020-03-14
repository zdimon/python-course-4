print("Making recousion coctail!!!")

def make(water,alcohol,cnt):
    cnt = cnt + 1
    mix = 0
    mix = mix + (water*30)
    mix = mix + (alcohol*20)
    if cnt > 10:
        return mix
    mix = mix + (make(water,alcohol,cnt)*50)
    print("process %s" % mix)
    return mix

    
    
cnt = 0    
print(make(3,4,cnt))
