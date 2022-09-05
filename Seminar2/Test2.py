#Напишите программу, которая принимает на вход число N и
#выдаёт последовательность из N членов.
#    - Для N = 5: 1, -3, 9, -27, 81

number = int(input('Enter your number: '))
numbers = [1]

for i in range(number-1):
    num = (numbers[i] * -3)
    numbers.append(num)

print(numbers)