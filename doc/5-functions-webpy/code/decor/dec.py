

def p_decorator(func):
    def wrapper(name):
        return '<p>%s</p>' % func(name)
    return wrapper

@p_decorator
def get_text(name):
    return "Hello, {0}".format(name)

print(get_text('Robert'))

