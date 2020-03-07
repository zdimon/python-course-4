print("Strings working")
ms = 'My string'
#print(ms[4:])
#ms[1] = 'e'
#ns = ms.replace('M','Y')
#print(ns)
#s = 'Hello %s my name is %s I am %d yo' % ('World!','Dima', 41)
#print(s)
#str = 'x = {x_coord}, y = {y_coord:d}'.format(x_coord=23,y_coord=56) 
#num = 123456789
#print('{:}'.format(num))
'''
month = '{:05d}'.format(3)
print(month)
print('{:.2f}'.format(22.445566))

import datetime

now = datetime.datetime.now()
print("Now is %s" % now)
print("Format now is {:%Y-%m-%d %H:%M:%S}".format(now))
'''

st = 'one,two,three'
#lst = st.split(',')
#print('----'.join(lst))
n = st.find('two0000000')
#print(n)

import re
str = 'My name is dima.'
rez = re.search(' is(.*)\.',str)
print(rez.group(1))