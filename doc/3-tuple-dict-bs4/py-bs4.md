## Библиотека BeatifulSoup.

Установка.

    pip install bs4
    
## пример html документа

    html_document = '''    
    <html>
        <head>
	        <title>Главная страница</title>
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
        
    
### Чтение DOM.

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_doc, 'html.parser')
    
Заголовок документа.

    soup.title.string


### Поиск одного и группы элементов.

    el = soup.find('h1')

Найдем все ссылки на странице.

    soup.findAll('a')
    
Доступ к тексту и атрибутам тега.

    link.get('href')
    link.text
    
Проход по массиву

    for link in soup.findAll('a'):
        print(link.get('href'))
        
Поиск одного элемента по id.

    el = soup.find('h1',{'id': 'my-header'})

Поиск многих элементов по имени класса.

    els = soup.findAll('div',{'class': 'class_name'})
    
по нескольким классам

    show = soup.find('div', class_='action-link showPhonesLink')
    show = soup.find('div', attrs={'class': 'action-link showPhonesLink'})

Поиск по css атрибутам.

    els = soup.findAll('div',attrs={'id': '123'})    
    
### Метод select

    results = soup.select('td[valign="top"]')    
    
- возвращает массив




