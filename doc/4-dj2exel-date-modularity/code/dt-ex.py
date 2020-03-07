import datetime
from time import strftime
from datetime import timedelta
#print("Current date")
#print(datetime.datetime.now().time())

#print(now.strftime("%Y-%m-%d %H:%M"))
#d = now - timedelta(days=6)
#for n in range(5):
#    dt = now - timedelta(days=n)
#    print(dt.strftime("%Y-%m-%d"))
#now = datetime.datetime.now()
#print(now.ctime())

#d = datetime.date(year=2008,month=3,day=1)
#print(d)

#from dateutil.relativedelta import relativedelta

#date_after_month = datetime.datetime.today() + relativedelta(months=1)
#print ('Today: %s' % datetime.datetime.today().strftime('%d/%m/%Y'))
#print ('After Month: %s' % date_after_month.strftime('%d/%m/%Y'))

#print(date_after_month.replace(year=2000))

t1 = datetime.time(14, 55, 0)
t2 = datetime.time(13,56,0)
print(t1<t2)