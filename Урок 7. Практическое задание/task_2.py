"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.

Хотя в примерах к уроку уже есть вариант реализации слияния,
попробуйте предложить другой (придумать или найти).

И попытаться сделать замеры на массивах разной длины: 10, 100, 1000, ...

Пример:
Введите число элементов: 5
Исходный - [46.11436617832828, 41.62921998361278, 18.45859540989644, 12.128870723745806, 8.025098788570562]
Отсортированный - [8.025098788570562, 12.128870723745806, 18.45859540989644, 41.62921998361278, 46.11436617832828]
"""
import random
from timeit import timeit


def merge(left_list, right_list):
    sorted_list = []
    left_list_index = right_list_index = 0

    # Длина списков часто используется, поэтому создадим переменные для удобства
    left_list_length, right_list_length = len(left_list), len(right_list)

    for _ in range(left_list_length + right_list_length):
        if left_list_index < left_list_length and right_list_index < right_list_length:
            # Сравниваем первые элементы в начале каждого списка
            # Если первый элемент левого подсписка меньше, добавляем его
            # в отсортированный массив
            if left_list[left_list_index] <= right_list[right_list_index]:
                sorted_list.append(left_list[left_list_index])
                left_list_index += 1
            # Если первый элемент правого подсписка меньше, добавляем его
            # в отсортированный массив
            else:
                sorted_list.append(right_list[right_list_index])
                right_list_index += 1

        # Если достигнут конец левого списка, элементы правого списка
        # добавляем в конец результирующего списка
        elif left_list_index == left_list_length:
            sorted_list.append(right_list[right_list_index])
            right_list_index += 1
        # Если достигнут конец правого списка, элементы левого списка
        # добавляем в отсортированный массив
        elif right_list_index == right_list_length:
            sorted_list.append(left_list[left_list_index])
            left_list_index += 1

    return sorted_list


def merge_sort(nums):
    # Возвращаем список, если он состоит из одного элемента
    if len(nums) <= 1:
        return nums

    # Для того чтобы найти середину списка, используем деление без остатка
    # Индексы должны быть integer
    mid = len(nums) // 2

    # Сортируем и объединяем подсписки
    left_list = merge_sort(nums[:mid])
    right_list = merge_sort(nums[mid:])

    # Объединяем отсортированные списки в результирующий
    return merge(left_list, right_list)



nums_el = int(input('Введите число элементов: '))
lst_start = [random.triangular(0, 50) for _ in range(nums_el)]
print(f'Исходный: {lst_start}')
lst_sort = merge_sort(lst_start)
print(f'Отсортированный: {lst_sort}')

# замеры на списке из 10 элементов
lst_start = [random.triangular(0, 50) for _ in range(10)]
print(f"Время выполнения на списке из 10 элементов - "
      f"{timeit('merge_sort(lst_start)', globals=globals(), number=1000)} сек")

# замеры на списке из 100 элементов
lst_start = [random.triangular(0, 50) for _ in range(100)]
print(f"Время выполнения на списке из 100 элементов - "
      f"{timeit('merge_sort(lst_start)', globals=globals(), number=1000)} сек")
# замеры на списке из 1000 элементов
lst_start = [random.triangular(0, 50) for _ in range(1000)]
print(f"Время выполнения на списке из 1000 элементов - "
      f"{timeit('merge_sort(lst_start)', globals=globals(), number=1000)} сек")
# Время выполнения на списке из 10 элементов - 0.03362580000000026 сек
# Время выполнения на списке из 100 элементов - 0.48340150000000026 сек
# Время выполнения на списке из 1000 элементов - 6.5670112 сек
# Вывод: сортировка слиянием достаточно эффективна, так как рост скорости работы
# функции увеличивается не сильно на массиве большой длины