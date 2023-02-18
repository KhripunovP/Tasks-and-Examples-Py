# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

num_1 = int(input("Введите количество элементов массива: "))
list = []
for i in range(num_1):
    list.append(random.randint(0, 10))
print(f'Массив {list}')

min = int(input("Введите нижнюю границу диапазона: "))
max = int(input("Введите верхнюю границу диапазона: "))
small_list =[]
for i in range (len(list)):
    if list[i] > min and list [i] < max:
        small_list.append(i)
print(f"Индексы элементов, значения которых находятся в заданном диапазоне: {small_list}")

