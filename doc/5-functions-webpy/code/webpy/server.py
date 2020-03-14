import web
from urlparse import urlparse, parse_qs
render = web.template.render('templates/')
db = web.database(dbn='postgres', user='postgres', pw='1q2w3e', db='users', host='localhost')
urls = (
    '/news/(\d+)', 'news',
    '/(.*)', 'hello'
    
)
app = web.application(urls, globals())

class news:
    def GET(self,id):
        return 'My news' + id

class hello:  

    def POST(self,req):
        data = web.data()      
        print(parse_qs(data))


    def GET(self, name):
        
        users = db.select('users')
        #t = db.transaction()
        #db.insert('users', name="Bob")
        #db.insert('users', name="Bob")
        #db.insert('users', name="Bob")
        #db.insert('users', name="Bob")
        #t.commit()
        return render.index(name, users)

if __name__ == "__main__":
    app.run()
