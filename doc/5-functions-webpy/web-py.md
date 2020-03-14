#WEB.PY

## Установка 

    pip install web.py

## Использование.


Простейшее веб приложение сервер.

    import web

    urls = (
        '/', 'hello'
    )

    app = web.application(urls,globals())#1

    class hello:
        def GET(self):
            return "Hello world!"

    if __name__ == "__main__":
        app.run()
    
1 - globals это функция, возвращающая словарь который содержит все переменные, определенные в глобальном прострастве.

Если она вызывается из функции, то возвратит словарь пространства того модуля, где ф-ция была определена а не где ее вызвали.

    
### Запуск на порту 8989.

    python server.py 8989    
    

### Определение параметра в URL.

    import web
            
    urls = (
        '/(.*)', 'hello'
    )
    app = web.application(urls, globals()) 

    class hello:        
        def GET(self, name):
            if not name: 
                name = 'World'
            return 'Hello, ' + name + '!'

    if __name__ == "__main__":
        app.run()


![web.py]({path-to-subject}/images/1.png)     


###URL обработака (роутинг)

    urls = (
        '/', 'index',
        /news', 'news',
        '/view_news/(\d+)', 'view_news',
        
    )

    class index: 
        ...
    class news: 
        ...
    class view_news: 
        def GET(self, id):
            """ View single news """
            post_id = int(id)


###Templating

Let's make a new directory for our templates (we'll call it templates). 
Inside, make a new file whose name ends with HTML (we'll call it index.html). 
Now, inside, you can just write normal HTML


    <em>Hello</em>, world!

Or you can use web.py's templating language to add code to your HTML:


    $def with (name)

    $if name:
        I just wanted to say <em>hello</em> to $name.
    $else:
        <em>Hello</em>, world!

Under the first line, add:

    import web
    render = web.template.render('templates/')


    
    ....
    def GET(self, name):
        return render.index(name)


## Databasing

###Installing MySQLdb

    pip install MySQL-python

First you need to create a database object.


    db = web.database(dbn='postgres', user='username', pw='password', db='dbname')


    def GET(self, name):
        users = db.select('user')
        out = 'Hello '
        for u in users:
            out = out+' '+u.name
        return out

###Output 

    Hello  dmitry sergey

### Insert records

    class insert:        
    def GET(self, name):
        n = db.insert('user', name=name)
        return 'Ok'





