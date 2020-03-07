import os
print("OS module!")
import shutil

path = os.path.join('one','two')
print(path)

#with open('147.txt','r') as f:
data = os.listdir('.')
for d in data:
    if os.path.isdir(d):
        print("Directory is %s" % d)
    else:
        print("File is %s" % d)


print("List directory")

lst = os.listdir('.')

print(lst)

'''
if os.path.isdir('year'):
    print("Deleting year dir")
    shutil.rmtree('year')

import random

for i in range(0,5):
    rnd = random.randint(100, 200)
    f = open(str(rnd)+'.txt','w')
    f.write(str(rnd))
    f.close()
    print("Creating file %s" % rnd)
    

print(__file__)

print(os.path.realpath(__file__))

print(os.path.dirname(os.path.realpath(__file__)))


newdir = 'new'
try:
    os.mkdir(newdir)
except:
    print('Fail!!!!')
'''

#path = "year/month/week/day"
#os.makedirs(path)

#os.rmdir('new')