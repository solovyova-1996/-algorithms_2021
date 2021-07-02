"""
Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-функции.
Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и множества
Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""


def search_substring(string, set_substring):
    for i in range(1,len(string)):
        set_substring.add(hash(string[:i]))
    for i in range(len(string)):
        set_substring.add(hash(string[-i:]))
        set_substring.add(hash(string[i]))
    return len(set_substring)

set_substring_test = set()
string_test = 'papa'
test_func = search_substring(string_test,set_substring_test)
print(test_func)
print(set_substring_test)
