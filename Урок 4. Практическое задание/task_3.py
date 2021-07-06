"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


#############################################################################
# мой вариант функций реверс числа
def revers_4(enter_num):
    # return str(enter_num)[::-1]
    return "".join(reversed(str(enter_num)))


def revers_5(enter_num):
    new_str = str()
    for i in str(enter_num)[::-1]:
        new_str += i
    return new_str


# замеры времени работы функции с помощью cProfile
def main():
    enter_num = 123
    for i in range(10000):
        res_1 = revers_1(enter_num)
        res_2 = revers_2(enter_num)
        res_3 = revers_3(enter_num)
        res_4 = revers_4(enter_num)
        res_5 = revers_5(enter_num)


enter_num = 123
run('main()')
# замеры времени работы функций с помощью timeit
print(f'Время выполнения функции: '
      f'{timeit("revers_1(enter_num)", globals=globals(), number=1000000)}')
# Время выполнения функции: 1.7473840000000003
print(f'Время выполнения функции: '
      f'{timeit("revers_2(enter_num)", globals=globals(), number=1000000)}')
# Время выполнения функции: 1.2731224
print(f'Время выполнения функции: '
      f'{timeit("revers_3(enter_num)", globals=globals(), number=1000000)}')
# Время выполнения функции: 0.6889204000000002
print(f'Время выполнения функции: '
      f'{timeit("revers_4(enter_num)", globals=globals(), number=1000000)}')
# Время выполнения функции: 1.2311821000000003
print(f'Время выполнения функции: '
      f'{timeit("revers_5(enter_num)", globals=globals(), number=1000000)}')
# Время выполнения функции: 1.2537867

# Вывод: наиболее эффективна функция revers_3(), выполняется минимум в 2 раза быстрее остальных функций,
# так как в этом варианте функции нет ветвления и циклов и выполняется только
# срез с конца строки, не создается новый объект
