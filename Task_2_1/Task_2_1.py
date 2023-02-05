# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
# *Пример:
# 5 -> 1 0 1 1 0
# 2
# *
import random

coins_number = int(input("Введите количество монет: "))
coins_list = []
for i in range(coins_number):
    coins_list.append(random.randint(0, 1))
print(coins_list)

side1_coin = coins_list.count(0)
side2_coin = coins_list.count(1)

print(side1_coin)
print(side2_coin)

if side1_coin >= side2_coin:
    print(f"Количество монет, которое нужно перевернуть: {side2_coin}")
else:
    print(f"Количество монет, которое нужно перевернуть: {side1_coin}")

