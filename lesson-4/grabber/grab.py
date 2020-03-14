import requests
from bs4 import BeautifulSoup

print('Start working!!!')

mainpage = requests.get('https://pythondigest.ru/')


soup = BeautifulSoup(mainpage.text, 'html.parser')


# h2s = soup.findAll('h2')

# for i in h2s:
#     print(i.text)


divs = soup.findAll('div', {"class": "items-group-container"})

for i in divs:
    link = i.find('a')
    print(link.text)


links = soup.findAll('a',{'class': 'issue-item-title'})

for link in links:
    print(link['href'])
    print(link.text)

'''

ДЗ

Сохранить все ссылки и их названия в json файл на диске.

С сайта https://pythondigest.ru/



'''

