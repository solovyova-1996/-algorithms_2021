"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш.

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей.

Самый просто вариант хранения хешей - просто в оперативной памяти (в переменных).

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Обязательно усложните задачу! Добавьте сохранение хеша в файле и получение его из файла.
А если вы знаете как через Python работать с БД, привяжите к заданию БД и сохраняйте хеши там.
"""
from uuid import uuid4
from hashlib import sha256
import sqlite3

connection = sqlite3.connect('cach_passw.db')
cursor = connection.cursor()
cursor.execute('''DROP TABLE IF EXISTS storage_passw''')
cursor.execute('''CREATE TABLE IF NOT EXISTS storage_passw 
(id INT,passw TEXT)''')
connection.commit()
connection.close()


def cache_sql():
    password = input('Введите пароль: ')
    salt = uuid4().hex
    password_hash = sha256(salt.encode() + password.encode()).hexdigest()
    print(f'В базе данных хранится строка: {password_hash}')
    connection = sqlite3.connect('cach_passw.db')
    cursor = connection.cursor()
    cursor.execute("INSERT INTO storage_passw (id,passw) VALUES (?,?)",
                   (1, password_hash))
    connection.commit()
    password_1 = input('Введите пароль еще раз для проверки: ')
    password_hash_1 = sha256(salt.encode() + password_1.encode()).hexdigest()
    cursor.execute("SELECT passw FROM storage_passw WHERE id = 1")
    results = cursor.fetchall()
    password_hash = results[0][0]
    connection.close()
    if password_hash == password_hash_1:
        print('Вы ввели верный пароль')


a = cache_sql()


def cache():
    password = input('Введите пароль: ')
    salt = uuid4().hex
    password_hash = sha256(salt.encode() + password.encode()).hexdigest()
    print(f'В базе данных хранится строка: {password_hash}')
    with open('file1.json', 'w', encoding='UTF-8') as f:
        f.write(password_hash)
    password_1 = input('Введите пароль еще раз для проверки: ')
    password_hash_1 = sha256(salt.encode() + password_1.encode()).hexdigest()
    with open('file1.json', 'r', encoding='UTF-8') as f:
        password_hash = f.read()

    if password_hash == password_hash_1:
        print('Вы ввели верный пароль')


b = cache()
