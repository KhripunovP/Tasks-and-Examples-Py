# Задаем с клавиатуры максимальную степень многочлена
# Формируется многочлен, пример ниже:
# 54*x**5 - 23*x**4 + 13*x**3 - 23*x**2 + 34*x - 78 = 0
# Сгенерировать второй и сложить их
import random

# Создали первый многочлен
exp_1 = int(input('Введите степень многочлена 1: '))
equation_1 = list()
for i in range(exp_1):
    koef = random.randint(-100, 100)
    if koef > 0 and i>0:
        equation_1.append(f'+{koef}*x**{exp_1-i}')
    elif koef == 0:
        continue
    else:
        equation_1.append(f'{koef}*x**{exp_1 - i}')

last_koef = random.randint(-100, 100)
if last_koef > 0:
    equation_1.append(f'+{last_koef} = 0')
else:
    equation_1.append(f'{last_koef} = 0')

print('Первый многочлен: ')
print(equation_1)

# Создали второй многочлен
exp_2 = int(input('Введите степень многочлена 2: '))
equation_2 = list()
for i in range(exp_2):
    koef = random.randint(-100, 100)
    if koef > 0 and i > 0:
        equation_2.append(f'+{koef}*x**{exp_2-i}')
    elif koef == 0:
        continue
    else:
        equation_2.append(f'{koef}*x**{exp_2 - i}')

last_koef = random.randint(-100, 100)
if last_koef > 0:
    equation_2.append(f'+{last_koef} = 0')
else:
    equation_2.append(f'{last_koef} = 0')

print('Второй многочлен: ')
print(*equation_2)

#Складываем многочлены
sum_equation = list()
length_1 = len(equation_1)
length_2 = len(equation_2)

part_1_1 = equation_1[:exp_1]
part_1_2 = equation_1[exp_1:]

part_2_1 = equation_2[:exp_2]
part_2_2 = equation_1[exp_2:]

if length_1 >= length_2:
    diff = length_1 - length_2
    part_1_3 = part_1_1[diff:]
    part_for_insert = equation_1[:diff]
    for i in range(exp_2):
        koef_of_first = part_1_3[i]
        num_1 = koef_of_first.split('*')
        koef_for_sum_1 = int(num_1[0])

        koef_of_second = part_2_1[i]
        num_2 = koef_of_second.split('*')
        koef_for_sum_2 = int(num_2[0])

        sum_koef = str(koef_for_sum_1 + koef_for_sum_2)
        sum_koef = sum_koef + (f'*x**{exp_2 - i}')
        sum_equation.append(sum_koef)

    for i in range(diff):
        sum_equation.insert(0, part_for_insert[i])
    # sum_equation.append(part_1_2[0])


print('Сумма многочленов: ')
print(*sum_equation)

# else:
#     diff = length_2 - length_1
#     list_2 = equation_2[diff:]