# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.
# Пример:
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

import random

num_1 = int(input("Введите количество элеиентов первого набора чисел:"))
num_list_1 = []
print("Введите элементы первого набора")
for i in range(num_1):
    num_list_1.append(input())
print(num_list_1)

num_2 = int(input("Введите количество элеиентов второго набора чисел:"))
num_list_2 = []
print("Введите элементы второго набора")
for i in range(num_2):
    num_list_2.append(input())
print(num_list_2)

new_list = []
for item in num_list_1:
    if num_list_2.count(item) != 0:
        new_list.append(item)
if len(new_list) > 0:
    print('Числа, которые встречаются в обоих наборах:')
    print(sorted(set(new_list)))
else:
    print('Нет чисел, которые бы встречались в обоих наборах')
