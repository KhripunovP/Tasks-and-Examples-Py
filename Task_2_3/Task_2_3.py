# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input("Введите число "))
list_of_multiplication = [1]
mult = 1

while mult <= number:
    mult = mult * 2
    if mult > number:
        break
    list_of_multiplication.append(mult)
print(*list_of_multiplication)
