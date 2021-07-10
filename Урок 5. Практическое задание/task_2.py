"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import defaultdict

d_default = defaultdict(list)
num_1 = list(input("Введите первое число: "))
d_default[1] = num_1
num_2 = list(input("Введите второе число: "))
d_default[2] = num_2
num_1_int = int(''.join(num_1), 16)
num_2_int = int(''.join(num_2), 16)


def sum_num(num_1, num_2):
    sum_number = num_1 + num_2
    res = hex(sum_number)[2:]
    return list(res)


def mul_num(num_1, num_2):
    mul_number = num_1 * num_2
    res = hex(mul_number)[2:]
    return list(res)


res_sum = sum_num(num_1_int, num_2_int)
res_mul = mul_num(num_1_int, num_2_int)
print(f"Сумма чисел из примера: {res_sum}")
print(f"Произведение: {res_mul}")


########################  ООП  #######################
class HexNumber:

    def __init__(self, number):
        self.number = number

    def __add__(self, other):
        new_num = int(self.number, 16) + int(other.number, 16)
        new_num = hex(new_num)
        return HexNumber(new_num[2:])

    def __mul__(self, other):
        new_num = int(self.number, 16) * int(other.number, 16)
        new_num = hex(new_num)
        return HexNumber(new_num[2:])


number_1 = list(input('Введите первое число: '))
number_2 = list(input('Введите второе число: '))
number_1_int = ''.join(number_1)
number_2_int = ''.join(number_2)
hex_num_1 = HexNumber(number_1_int)
hex_num_2 = HexNumber(number_2_int)
new_sum = hex_num_1 + hex_num_2
new_mul = hex_num_1 * hex_num_2
new_sum_lst = list(new_sum.number)
new_mul_lst = list(new_mul.number)
print(f"Сумма чисел из примера: {new_sum_lst}")
print(f"Произведение: {new_mul_lst}")
