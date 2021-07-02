"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
from uuid import uuid4
from hashlib import sha256


def cache_web(url, cache):
    if cache.get(url) is None:
        salt = uuid4().hex
        cache[url] = sha256(salt.encode() + url.encode()).hexdigest()


cache_1 = dict()
# 2 одинаковых url
url_1 = 'https://edu.omgpu.ru/login/index.php'
url_2 = 'https://edu.omgpu.ru/login/index.php'
# url отличается
url_3 = 'https://gb.ru/'
# вызов функции с url
res_1 = cache_web(url_1, cache_1)
res_2 = cache_web(url_2, cache_1)
res_3 = cache_web(url_3, cache_1)
# просмотр заполненного словаря
print(cache_1)
