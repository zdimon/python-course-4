import requests
'''
date = '2018-01-01'
url = 'https://api-football-v1.p.rapidapi.com/fixtures/date/%s' % date
headers={
    "X-RapidAPI-Host": "api-football-v1.p.rapidapi.com",
    "X-RapidAPI-Key": "4992332789mshfb7baebbf8e1951p154cc3jsn9a44c55acbda"
  }
r = requests.get(url,headers=headers)
filename = '%s.json' % date
with open(filename,'w+') as f:
    f.write(r.text)
print("Done!")
'''

url = 'https://webmonstr.com/ru/login/'

data = {"username": "test", "password": "test"}

r = requests.post(url,data=data)
print(r.text)






