
def empty_func():
    pass

def add(*args): # переменное число ПОЗИЗИОННЫХ агрументов
    print(args)
    resullt = 0
    for v in args:
        resullt = resullt + v
    return resullt

#print(add(2,2,3,4,5,6))

def multi(**kwargs): #переменное число ИМЕНОВАННЫХ агрументов
    res = 1
    for key, value in kwargs.items():
        res = res*value
    return res

#rint(multi(a=5,b=5,c=6))

def add_multi(*args,**kwargs):
    for a in args:
        print('List arg: %s' % a)
        
    for k,v in kwargs.items():
        print('key: %s  value: %s' % (k,v))

print(add_multi(1,2,3,s=3,y=8))