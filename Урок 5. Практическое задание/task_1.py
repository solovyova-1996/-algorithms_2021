"""
1.	Пользователь вводит данные о количестве предприятий, их наименования и прибыль
за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections.

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Фирма_1
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Фирма_2
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Фирма_1

Предприятия, с прибылью ниже среднего значения: Фирма_2
"""
from collections import namedtuple
from statistics import mean


def fill_template(count_firm):
    lst_firm = []
    lst_profit = []
    for i in range(count_firm):
        name_firm = input('Введите название предприятия: ')
        profit = input('через пробел введите прибыль данного предприятия '
                       'за каждый квартал(Всего 4 квартала):').split()
        try:
            profit_lst_int = [float(i) for i in profit]
        except ValueError:
            print("Неверные данные, необходимо ввести числа через пробел")
            profit = input(
                'через пробел введите прибыль данного предприятия '
                'за каждый квартал(Всего 4 квартала):').split()
            profit_lst_int = [float(i) for i in profit]
        lst_firm.append(name_firm)
        lst_profit.append(sum(profit_lst_int))
    Storage = namedtuple('Storage', lst_firm)
    res = Storage._make(lst_profit)
    return res


def min_profit(dict_firm_profit, avg_profit):
    str_firm = str()
    for key, val in dict_firm_profit.items():
        if val < avg_profit:
            str_firm += key + ' '
    return str_firm


def max_profit(dict_firm_profit, avg_profit):
    str_firm = str()
    for key, val in dict_firm_profit.items():
        if val > avg_profit:
            str_firm += key + ' '
    return str_firm


try:
    count_firm_input = int(input('Введите количество предприятий '
                                 'для расчета прибыли: '))
except ValueError:
    print("Неверные данные, необходимо ввести число")
    count_firm_input = int(input('Введите количество предприятий '
                                 'для расчета прибыли: '))
res = fill_template(count_firm_input)
avg_profit = mean(res)
print(f'Средняя годовая прибыль всех предприятий: {avg_profit}')

dict_firm_profit = res._asdict()
max_profit_firm = max_profit(dict_firm_profit, avg_profit)
min_profit_firm = min_profit(dict_firm_profit, avg_profit)
print(f"Предприятия, с прибылью выше среднего значения: {max_profit_firm}")
print(f"Предприятия, с прибылью ниже среднего значения: {min_profit_firm}")
