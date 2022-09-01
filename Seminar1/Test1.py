# Напишите программу, которая принимает на вход два числа
# и проверяет, является ли одно число квадратом другого.


number_1 = int(input("Enter number1 "))
number_2 = int(input("Enter number2 "))

if (number_2 == (number_1 ** 2)) or (number_1 == (number_2 ** 2)):
    print(True)
else:
    print(False)
