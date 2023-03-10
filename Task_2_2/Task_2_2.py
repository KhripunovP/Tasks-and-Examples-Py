# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
# *Пример:
# 4 4 -> 2 2
# 5 6 -> 2 *
import math

sum = int(input("Введите сумму чисел: "))
prod = int(input("Введите произведение чисел: "))

# sum = x + y
# prod = x * y
# x = sum - prod / x
# Итоговое уравнение:
# x * x - sum * x + prod = 0

discr = sum**2 - 4 * prod

if discr > 0:
    x = (sum + math.sqrt(discr)) / 2
    y = (sum - math.sqrt(discr)) / 2
    print (f"Первое число равно {round(x,2)}, второе число равно {round(y, 2)}")
elif discr == 0:
    x = sum / 2
    print (f"Числа равны {round(x, 2)}")
else:
    print ("таких чисел нет")