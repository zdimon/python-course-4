import requests
import bs4
url = 'https://www.crummy.com/software/BeautifulSoup/bs4/doc/#'

rez = requests.get(url)
#print(rez.text)
soup = bs4.BeautifulSoup(rez.text,'html.parser')

'''
#div = soup.findAll('div',attrs={'class':"section"})
divs = soup.select('div[class="section"]')
for div in divs:
    for link in div.findAll('a'):
        print(link.text)

'''

div = soup.find('div',id="quick-start")
next = div.find_next()
print(next)
next = next.find_next()
print(next)
