# Напишите программу, которая на вход принимает 5 чисел
# и находит максимальное из них.

numbers = []

for i in range(5):
    numbers.append(int(input('Input number: ')))
print('Build in function max: ', max(numbers))
maxx = numbers[0]
max2 = numbers[0]
for i in numbers[1:]:  # проверка с индекса 1 до конца (срез)
    if i > maxx:
        maxx = i

for i in range(len(numbers)):  # проверка используя индексы списка
    if numbers[i] > max2:
        max2 = numbers[i]

print(maxx)
print(max2)