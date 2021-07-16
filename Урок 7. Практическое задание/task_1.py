"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
"""Сортировка пузырьком"""

import timeit
import random


################## Оригинальная функция из примера в уроке #####################

def bubble_sort(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] > lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# замеры 10
# orig_list = [random.randint(-100, 100) for _ in range(10)]
# print(
#     timeit.timeit(
#         "bubble_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))
#
# orig_list = [random.randint(-100, 100) for _ in range(100)]
#
# # замеры 100
# print(
#     timeit.timeit(
#         "bubble_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))
#
# orig_list = [random.randint(-100, 100) for _ in range(1000)]
#
# # замеры 1000
# print(
#     timeit.timeit(
#         "bubble_sort(orig_list[:])",
#         globals=globals(),
#         number=1000))

# 0.06876350000000003
# 1.7818022999999998
# 166.9776324
############################ пузырек по убыванию ###############################
def bubble_sort_waning(lst_obj):
    n = 1
    while n < len(lst_obj):
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
        n += 1
    return lst_obj


# замеры 10
# orig_list = [random.randint(-100, 100) for _ in range(10)]
# print(
#     timeit.timeit(
#         "bubble_sort_waning(orig_list[:])",
#         globals=globals(),
#         number=1000))
#
# orig_list = [random.randint(-100, 100) for _ in range(100)]
#
# # замеры 100
# print(
#     timeit.timeit(
#         "bubble_sort_waning(orig_list[:])",
#         globals=globals(),
#         number=1000))
#
# orig_list = [random.randint(-100, 100) for _ in range(1000)]
#
# # замеры 1000
# print(
#     timeit.timeit(
#         "bubble_sort_waning(orig_list[:])",
#         globals=globals(),
#         number=1000))
# 0.02145549999999999
# 2.9664789
# 136.9452684

################# пузырек улучшеный № 1 ###############################
# пузырек по убыванию и при сортированнном списке выходит из цикла,
# что дает потенциальное увеличение скорости
def bubble_sort_waning_update(lst_obj):
    n = 1
    change_count = 0
    while n < len(lst_obj):
        if n == 2 and change_count == 0:
            print(1)
            break
        for i in range(len(lst_obj) - n):
            if lst_obj[i] < lst_obj[i + 1]:
                lst_obj[i], lst_obj[i + 1] = lst_obj[i + 1], lst_obj[i]
                change_count += 1

        n += 1
    return lst_obj


# замеры 10

orig_list = [random.randint(-100, 100) for _ in range(10)]
print(
    timeit.timeit(
        "bubble_sort_waning_update(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(100)]

# замеры 100
print(
    timeit.timeit(
        "bubble_sort_waning_update(orig_list[:])",
        globals=globals(),
        number=1000))

orig_list = [random.randint(-100, 100) for _ in range(1000)]

# замеры 1000
print(
    timeit.timeit(
        "bubble_sort_waning_update(orig_list[:])",
        globals=globals(),
        number=1000))
# 0.019133700000000003
# 1.9433184
# 239.9567904

# вывод: выход из цикла при попаданиии в функцию отсортированного списка
# дает только потенциальное увеличение скорости работы функции, то есть функция
# отработаем быстрее только если массив будет отсортирован, на большом массиве
# происходит замедление функции bubble_sort_waning_update, в сравнении с функцией bubble_sort

