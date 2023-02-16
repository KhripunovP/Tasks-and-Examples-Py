# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии

def function_exp(a, exp):
    if exp == 1:
        return a
    elif exp == 0:
        return 1
    else:
        res_exp = a * function_exp(a, exp - 1)
        return res_exp

num_1 = int(input("Введите число: "))
num_2 = int(input("Введите степень числа: "))
print(function_exp(num_1, num_2))

