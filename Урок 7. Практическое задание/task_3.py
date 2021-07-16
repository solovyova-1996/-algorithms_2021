"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом.
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на
две равные по длине части: в одной находятся элементы, которые не меньше медианы,
в другой – не больше медианы.

Задачу можно решить без сортировки исходного массива.

Но если это слишком сложно, то используйте метод сортировки,
который не рассматривался на уроках: Шелла, Гномья, Кучей...

Важно: стройте массив именно по формуле 2m+1
Потому что параметр m вам пригодится при поиске медианы, когда массив будет отсортирован.
Этот парамет m вам нужно запрашивать у пользователя.

[5, 3, 4, 3, 3, 3, 3]

[3, 3, 3, 3, 3, 4, 5]

my_lst
new_lts

arr[m]


from statistics import median

[3, 4, 3, 3, 5, 3, 3]

left = []
right = []

left == right and

for i in
    for
    left == right
    left.clear()
    right.clear()


"""
from statistics import median
import random
from timeit import timeit


############################ Сортировка Шелла  ##########################
def shell_sort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(alist, startposition, sublistcount)
        sublistcount = sublistcount // 2


def gap_insertion_sort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):

        currentvalue = alist[i]
        position = i

        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position = position - gap
            alist[position] = currentvalue




#################    Решение без сортировки  ###########################
def get_mediana(lst):
    len_lst = len(lst)
    n = 0
    while n < len_lst // 2:
        if lst[n] > lst[n + 1]:
            del lst[n]
        else:
            del lst[n + 1]
        n += 1
    return max(lst)


m = int(input('Введите параметр m: '))
alist = [random.randint(-100, 100) for _ in range(2 * m + 1)]

a = get_mediana(alist[:])
print(a)

#################    Решение с помощью функции median()  #######################
m = int(input('Введите параметр m: '))
alist = [random.randint(-100, 100) for _ in range(2 * m + 1)]

print(median(alist[:]))


######################## сортировка кучей ###################################
def heapify(nums, heap_size, root_index):
    # Предположим, что индекс самого большого элемента является корневым индексом
    largest = root_index
    left_child = (2 * root_index) + 1
    right_child = (2 * root_index) + 2

    if left_child < heap_size and nums[left_child] > nums[largest]:
        largest = left_child

    if right_child < heap_size and nums[right_child] > nums[largest]:
        largest = right_child

    if largest != root_index:
        nums[root_index], nums[largest] = nums[largest], nums[root_index]

        heapify(nums, heap_size, largest)


def heap_sort(nums):
    n = len(nums)
    for i in range(n, -1, -1):
        heapify(nums, n, i)

    for i in range(n - 1, 0, -1):
        nums[i], nums[0] = nums[0], nums[i]
        heapify(nums, i, 0)



# 11
alist = [random.randint(-100, 100) for _ in range(2 * 5 + 1)]
print(f"Время выполнения сортировки Шелла на массиве из 11 элементов: "
      f"{timeit('shell_sort(alist[:])', globals=globals(), number=1000)} сек")
# 101
alist = [random.randint(-100, 100) for _ in range(2 * 50 + 1)]
print(f"Время выполнения сортировки Шелла на массиве из 101 элементов: "
      f"{timeit('shell_sort(alist[:])', globals=globals(), number=1000)} сек")
# 1001
alist = [random.randint(-100, 100) for _ in range(2 * 500 + 1)]
print(f"Время выполнения сортировки Шелла на массиве из 1001 элементов: "
      f"{timeit('shell_sort(alist[:])', globals=globals(), number=1000)} сек")
# Время выполнения сортировки Шелла на массиве из 11 элементов: 0.017036200000000612 сек
# Время выполнения сортировки Шелла на массиве из 101 элементов: 0.29686900000000005 сек
# Время выполнения сортировки Шелла на массиве из 1001 элементов: 5.8712871 сек
lst = [random.randint(-100, 100) for _ in range(2 * 5 + 1)]
print(f"Время нахождения медианы без сортировки на массиве из 11 элементов: "
      f""f"{timeit('get_mediana(lst[:])', globals=globals(), number=1000)} сек")
lst = [random.randint(-100, 100) for _ in range(2 * 50 + 1)]
print(f"Время нахождения медианы без сортировки на массиве из 101 элементов: "
      f""f"{timeit('get_mediana(lst[:])', globals=globals(), number=1000)} сек")
lst = [random.randint(-100, 100) for _ in range(2 * 500 + 1)]
print(f"Время нахождения медианы без сортировки на массиве из 1001 элементов: "
      f"{timeit('get_mediana(lst[:])', globals=globals(), number=1000)} сек")
#Время нахождения медианы без сортировки на массиве из 11 элементов: 0.0022882000000006286 сек
# Время нахождения медианы без сортировки на массиве из 101 элементов: 0.02948380000000128 сек
# Время нахождения медианы без сортировки на массиве из 1001 элементов: 0.3353313999999994 сек
lst = [random.randint(-100, 100) for _ in range(2 * 5 + 1)]
print(f"Время работы функции median() на массиве из 11 элементов: "
      f"{timeit('median(lst[:])', globals=globals(), number=1000)} сек")
lst = [random.randint(-100, 100) for _ in range(2 * 50 + 1)]
print(f"Время работы функции median() на массиве из 101 элементов: "
      f"{timeit('median(lst[:])', globals=globals(), number=1000)} сек")
lst = [random.randint(-100, 100) for _ in range(2 * 500 + 1)]
print(f"Время работы функции median() на массиве из 1001 элементов: "
      f"{timeit('median(lst[:])', globals=globals(), number=1000)} сек")
# Время работы функции median() на массиве из 11 элементов: 0.0018917999999992219 сек
# Время работы функции median() на массиве из 101 элементов: 0.009664700000000082 сек
# Время работы функции median() на массиве из 1001 элементов: 0.19069350000000007 сек
alist = [random.randint(-100, 100) for _ in range(2 * 5 + 1)]
print(f"Время выполнения сортировки кучей на массиве из 11 элементов: "
      f"{timeit('heap_sort(alist[:])', globals=globals(), number=1000)} сек")
# 101
alist = [random.randint(-100, 100) for _ in range(2 * 50 + 1)]
print(f"Время выполнения сортировки кучей на массиве из 101 элементов: "
      f"{timeit('heap_sort(alist[:])', globals=globals(), number=1000)} сек")
# 1001
alist = [random.randint(-100, 100) for _ in range(2 * 500 + 1)]
print(f"Время выполнения сортировки кучей на массиве из 1001 элементов: "
      f"{timeit('heap_sort(alist[:])', globals=globals(), number=1000)} сек")
# Время выполнения сортировки кучей на массиве из 11 элементов: 0.032103799999999794 сек
# Время выполнения сортировки кучей на массиве из 101 элементов: 0.5408653999999995 сек
# Время выполнения сортировки кучей на массиве из 1001 элементов: 7.880576099999999 сек

# Вывод: наиболее оптимальным решением для нахождения медианы списка будет
# использование функции mediana(), так как скорость выполнения на массивах
# разной длины отличается незначительно, похожие результаты при нахождении медианы
# без сортировки. Использование сортировки "Шелла" и "Кучей" занимает примерно одинаковое время,
# сортировка Шелла чуть быстрее
