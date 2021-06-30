"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Массив в этом задании строить не нужно!
Нужно решить без него!

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


# def sum_numbers(count, sum_num=0.0, num=1.0):
#     if num < 0 and count > 0:
#         return sum_numbers(count - 1, sum_num + num, abs(num / 2))
#     elif num > 0 and count > 0:
#         return sum_numbers(count - 1, sum_num + num, -num / 2)
#     else:
#         return sum_num

def sum_numbers(count, sum_num=0.0, num=1.0):
    if count == 0:
        return sum_num
    else:
        return sum_numbers(count - 1, sum_num + num, abs(num / 2)) if num < 0 else sum_numbers(count - 1, sum_num + num, -num / 2)




count = 3
a = sum_numbers(count)
print(a)
