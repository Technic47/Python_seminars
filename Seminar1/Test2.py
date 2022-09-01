# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.


number_1 = int(input("Enter number1 "))
number_2 = int(input("Enter number2 "))
number_3 = int(input("Enter number3 "))
number_4 = int(input("Enter number4 "))
number_5 = int(input("Enter number5 "))

max = number_1

if number_2 > max:
    max = number_2
if number_3 > max:
    max = number_3
if number_4 > max:
    max = number_4
if number_5 > max:
    max = number_5

print(max)
