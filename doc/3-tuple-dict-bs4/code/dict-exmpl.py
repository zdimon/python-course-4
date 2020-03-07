print('Work with dictionaries')

mdict = {1: 'Zara', 'Age': 7, 'Class': 'First'}

mdict[1] = 'Dima'

#print(dict.get(1,'undefined'))
#del mdict[1]
#print(dict)

#dict[['one']] = '1111'

#md = dict(name='Vova', age=23)

#print(type(md))

#d1 = ['one', 'two', 'three']
#d2 = [1, 2, 3]
#d3 = dict(zip(d1,d2))
#d3 = dict.fromkeys(d1,d2)

#d4 = {"one": "11111111111"}

#d3.update(d4)

#print(d3)

#print(d3)
#print(d3.has_key('one')) # only for Python 2!
#for key in d3.keys():
#    print(d3[key])
#print(d3.values())

#for key, value in d3.items(): # For Python 3.x
#    print("key = %s value = %s" % (key,value))

import json
d1 = {"one": 1, "two": '2'}
s1 = json.dumps(d1)
#print(s1)

# write into file
f = open('tst.txt','w+')
f.write(s1)
f.close()

# read from file
f = open('tst.txt','r')
st = f.read()
f.close()
st_dict = json.loads(st)
print(st_dict['two'])





