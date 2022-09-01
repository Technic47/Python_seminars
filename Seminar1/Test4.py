# Напишите программу, которая будет на вход принимать число N
# и выводить числа от -N до N

number = int(input("Input number: "))

numbers = []

for i in range(-number, number + 1):
    print(i, end=' ')
