"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from timeit import timeit
from random import randint


######################## Заполнение  #######################
def filling_dict(count_repeat):
    new_dict = dict()
    for i in range(count_repeat):
        new_dict[i] = i
    return new_dict


def filling_ordereddict(count_repeat):
    new_ordereddict = OrderedDict()
    for i in range(count_repeat):
        new_ordereddict[i] = i
    return new_ordereddict


count_repeat = 100
# a = filling_dict(count_repeat)
# print(a)
# print('#################################')
# b = filling_ordereddict(count_repeat)
# print(b)
print(f"Время заполнения словаря: "
      f"{timeit('filling_dict(count_repeat)', globals=globals(), number=100)}")
print(f"Время заполнения Ordereddict: "
      f"{timeit('filling_ordereddict(count_repeat)', globals=globals(), number=100)}")


# Время заполнения словаря: 0.0018569000000000224
# Время заполнения Ordereddict: 0.002932999999999991
# Вывод: dict() заполняется примерно на 30% быстрее, чем Ordereddict()
# dict()  в версиях Python начиная от 3.6 также запоминают порядок добавления элементов
######################### Добавление элемента ##########################
def get_elem_dict(repeat, test_dict):
    for i in range(repeat):
        random_num = randint(1, 1000)
        a = test_dict.get(random_num)


def get_elem_ordereddict(repeat, test_ordereddict):
    for i in range(repeat):
        random_num = randint(1, 1000)
        a = test_ordereddict.get(random_num)


test_dict = filling_dict(1000)

test_ordereddict = filling_ordereddict(1000)
repeat = 1000
print(f"Получение элемента из dict(): "
      f"{timeit('get_elem_dict(repeat,test_dict)', globals=globals(), number=1)}")
print(f"Получение элемента из OrderedDict(): "
      f"{timeit('get_elem_ordereddict(repeat,test_ordereddict)', globals=globals(), number=1)}")

# Получение элемента из dict(): 0.004321400000000003
# Получение элемента из OrderedDict(): 0.00420100000000001
# вывод: получение элементов из dict() и OrderedDict() занимает одинаковое время
# общий вывод: словари dict() в версиях python от 3.6 повторяют функционал OrderedDict()
# сортировки по добавлению ключа, но OrderedDict() при использовании вместе с dict()
# дает дополнительные возможности сортировки, например сортировка по значению
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
f = OrderedDict(sorted(d.items(), key=lambda t: t[1]))
print(f)
# думаю, что есть смысл использовать OrderedDict() в Python 3.6 и более поздних версиях,
# напрмер когда необходимо отсортировать словарь