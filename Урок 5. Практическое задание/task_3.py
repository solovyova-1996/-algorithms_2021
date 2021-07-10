"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""
from collections import deque
from timeit import timeit
from random import randint


#########################  Операция наполнения ################################
# наполнение списка
def fill_lst(count_fill):
    lst = []
    for i in range(count_fill):
        lst.append(i)
    return lst


# наполнение очереди
def fill_deque(count_fill):
    new_deque = deque()
    for i in range(count_fill):
        new_deque.append(i)
    return new_deque


count_fill = 1000
print(f"Наполнение списка: "
      f"{timeit('fill_lst(count_fill)', globals=globals(), number=1)}")
print(f"Наполнение очереди: "
      f"{timeit('fill_deque(count_fill)', globals=globals(), number=1)}")


# Наполнение списка: 0.00023039999999999172
# Наполнение очереди: 0.00022969999999999935
# вывод: наполнение списка и наполнение очереди с использованием append()
# происходит приблизительно за одинаковое кол-во времени

##################  Операция удаления и возврата первого элемента ############


def popleft_deque(count_repeat, deque_test):
    for i in range(count_repeat):
        deque_test.popleft()


def popleft_lst(count_repeat, lst_test):
    for i in range(count_repeat):
        lst_test.pop(0)


deque_test = fill_deque(100000)
lst_test = fill_lst(100000)
count_repeat = 10000
print(f"Popltfet для очереди:"
      f" {timeit('popleft_deque(count_repeat, deque_test)', globals=globals(), number=1)}")
print(f"Для списка: "
      f"{timeit('popleft_lst(count_repeat, lst_test)', globals=globals(), number=1)}")


# Popltfet для очереди: 0.0011894999999999822
# Для списка: 1.3974869
# Вывод операция удаленияи возврата первого элемента для очереди выполняется
# в 1000 раз быстрее чем для списка
# deque() из модуля collections выигрывает по сравнению с list()

############  Операция добавления элемента в начало очереди/списка ############

def appendleft_deque(repeat):
    new_deque = deque()
    for i in range(repeat):
        new_deque.appendleft(i)
    return new_deque


def appendleft_lst(repeat):
    new_lst = []
    for i in range(repeat):
        new_lst.insert(0, i)
    return new_lst


repeat = 10000

print(f"Время вставки в начало для очереди: "
      f"{timeit('appendleft_deque(repeat)', globals=globals(), number=1)}")
print(f"Время вставки вначало для списка: "
      f"{timeit('appendleft_lst(repeat)', globals=globals(), number=1)}")


# Время вставки в начало для очереди: 0.014989200000000036
# Время вставки вначало для списка: 0.06729509999999994
# Вывод вставка элемента вначало очереди происходи примерно в 5-6 раз бастрее,
# чем вставка элемента вначало списка

############  Операция расширения(с начала) очереди/списка ############

def extendleft_deque(n):
    new_deque = deque()
    lst_extend = [i for i in range(n)]
    for i in range(n):
        new_deque.extendleft(lst_extend)
    return new_deque


def extendleft_lst(n):
    new_lst = []
    lst_extend = [i for i in range(n)]
    for i in range(n):
        for j in lst_extend:
            new_lst.insert(0, j)
    return new_lst


n = 100

print(f"Расширение очереди с начала: "
      f"{timeit('extendleft_deque(n)', globals=globals(), number=1)}")
print(f"Расширение списка с начала: "
      f"{timeit('extendleft_lst(n)', globals=globals(), number=1)}")


# Расширение очереди с начала: 0.0002238999999999436
# Расширение списка с начала: 0.10221440000000004
# Вывод: расширение очереди с начала(extendleft) происходит в ~500 раз быстрее,
# чем расширение списка при помощи insert()

################### Быстрый случайный доступ ####################

def return_random_elem_deque(n, deque_test_1):
    len_deque_test = len(deque_test_1) - 1
    for i in range(n):
        random_num = randint(1, len_deque_test)
        a = deque_test_1[random_num]


def return_random_elem_lst(n, lst_test_1):
    len_lst_test = len(lst_test_1) - 1
    for i in range(n):
        random_num = randint(1, len_lst_test)
        a = lst_test_1[random_num]


n = 100
deque_test_1 = fill_deque(100)
lst_test_1 = fill_lst(100)
print(f"Быстрый случайный доступ к элементу очереди: "
      f"{timeit('return_random_elem_deque(n, deque_test_1)', globals=globals(), number=1)}")
print(f"Быстрый случайный доступ к элементу списка: "
      f"{timeit('return_random_elem_lst(n, lst_test_1)', globals=globals(), number=1)}")


# Быстрый случайный доступ к элементу очереди: 0.013758900000000018
# Быстрый случайный доступ к элементу списка: 0.00020609999999998685
# Вывод: быстрый случайный доступ к элементу списка выполняется в ~100 раз быстрее,
# чем к элементу очереди

############  Операция расширения(с конца) очереди/списка ############

def extend_deque(n):
    new_deque = deque()
    lst_extend = [i for i in range(n)]
    for i in range(n):
        new_deque.extend(lst_extend)
    return new_deque


def extend_lst(n):
    new_lst = []
    lst_extend = [i for i in range(n)]
    for i in range(n):
        new_lst.extend(lst_extend)
    return new_lst


n = 100

print(f"Расширение очереди с конца: "
      f"{timeit('extend_deque(n)', globals=globals(), number=1)}")
print(f"Расширение списка с конца: "
      f"{timeit('extend_lst(n)', globals=globals(), number=1)}")

# Расширение очереди с конца: 0.0002468999999998278
# Расширение списка с конца: 0.00014559999999996798

# Общий вывод: специальные методы для deque() такие как popleft(),appendleft(),
# extendleft(), работают значительно быстрее, чем их аналогичная реализация
# при помощи стандартных методов списков, а одинаковые метода для deque() и list(),
# например, append(), extend() работают за приблизительно одинаковое время,
# случайный доступ к элементу быстрее для списка, чем для очереди
