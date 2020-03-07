print("Using library %s" % __name__)

GLOBAL_DOMAIN = 'domain.com'

def getDomain():
    return 'My domain is %s' % GLOBAL_DOMAIN

class app():
    typeApp = 'angular+python'
    author = 'Dimitry'
    def getBody(self):
        html = '<body> this is %s application of %s</body>' % (self.typeApp, self.author)
        return html 

if __name__ == '__main__':
    print("Running from the command line")