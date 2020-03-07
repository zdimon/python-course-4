## Библиотека requests.

[дока](https://2.python-requests.org//en/master/)

Установка.

    pip install requests

## Использование.

    import requests

Запрос с передачей хэдеров.

    r=requests.get(url, headers={"key":"val"})
    print(t.text)

## POST запрос

    url = 'https://webmonstr.com/ru/login/'
    data = {"username": "test", "password": "test"}
    r = requests.post(url,data=data)
    print(r.text)


























