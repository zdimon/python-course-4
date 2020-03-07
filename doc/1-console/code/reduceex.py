def reducer_func(el_prev, el):
    # el_prev - предшествующий элемент
    # el - текущий элемент
    return el_prev + el
from functools import reduce #python 3
print(reduce(reducer_func, [1, 2, 3]))