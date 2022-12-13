#Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
#Не использовать функцию bin

number = int(input())
result = ''
while number > 0:
     result += str(number % 2)
     number //= 2

print(result[::-1])# или print(bin(number)[2:])
