#2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
import random as r
random_lst = [r.randint(1, 5) for i in range(r.randint(4, 7))]
print('Список случайных чисел:', random_lst)
len_lst = len(random_lst)
mult_lst = [random_lst[i] * random_lst[-i - 1] for i in range(len_lst // 2)]
if len_lst % 2 == 1:
    mult_lst.append(random_lst[len_lst // 2] ** 2)
print('Список произведения пар чисел:', mult_lst)