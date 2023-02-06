# Первая задача:
# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению
import random

list_length = int(input("Задайте длину списка чисел: "))
numbers_list = []
for i in range(list_length):
    numbers_list.append(random.randint(0, 100))
print(numbers_list)

number_X = int(input("Введите число, которое будем искать в списке: "))
quantity_X = numbers_list.count(number_X)

if quantity_X == 0:
    print("Такого числа в списке нет")
    for i in range(1, 200, 1):
        delta = i * ((-1)**i)
        number_X = number_X + delta
        quantity_X = numbers_list.count(number_X)
        if quantity_X != 0:
            break
    print(f"Но есть ближайшее число {number_X}, таких в списке {quantity_X}")

else:
    print(f"Таких чисел в списке {quantity_X}")



