# Задайте список. Напишите программу, которая определит,
# присутствует ли в заданном списке строк некое число.
# ['65h34q', 'sdg634d', '147jnbv']
# "7"

lines = input('Enter your lines via space: ').split(' ')

print(lines)

number = input('Enter your number: ')

result = [i for i in lines if number in i]

if len(result) > 0:
    print(True)
else:
    print(False)
