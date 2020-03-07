import bs4

html_document = '''

<html>

    <head>
        <title> Главная страница </title>
    </head>

    <body>
        <h1> Заголовок H1  </h1>
        <a href="http://google.com"> Ссылка 1 </a>
        <a href="http://yandex.ru"> Ссылка 2 </a>  
        <div id="block_id">
            Блочный элемент
        </div>      
        <p class="p_class"> Параграф 1 </p>
        <p class="p_class"> Параграф 2 </p>
        <p class="p_class"> Параграф 3 </p>
        <table>
            <tr> 
                <td valign="top"> Ячейка 1 </td>
                <td valign="top"> Ячейка 1 </td>
                <td valign="top"> Ячейка 3 </td>    
            </tr>
            <tr> 
                <td valign="top"> Ячейка 1 </td>
                <td valign="top"> Ячейка 1 </td>
                <td valign="top"> Ячейка 3 </td>    
            </tr>
        </table>
    </body>
</html>

'''

soup = bs4.BeautifulSoup(html_document,'html.parser')
print(soup.title.string)

el = soup.find('h1')
print(el.text)

links = soup.findAll('a')

for link in links:
    print(link.get('href'))

ps = soup.findAll('p',{'class': 'p_class'})

print(ps)

div = soup.find('div',{'id': 'block_id'})

print(div.text)

res = soup.select('td[valign="top"]')

print(div.previous_sibling)