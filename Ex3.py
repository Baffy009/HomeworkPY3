#Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

float_list = [round(_ - int(_), 2) for _ in [1.1, 1.2, 3.1, 10.01]]
print(float_list)
print(round(max(float_list) - min(float_list), 3))