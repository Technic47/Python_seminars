# 1. В файле находится N натуральных чисел, записанных
# через пробел. Среди чисел не хватает одного, чтобы
# выполнялось условие A[i] - 1 = A[i - 1].Найдите это число.


path = r'C:\Users\Pavel\Documents\GeekBrain\Python\ Seminar5\Numbers.txt'
numbers = []
with open(path, 'r') as data:
    string = (data.read().split(' '))

numbers = list(map(int, string))

print(numbers)

# for i in range(1, len(numbers)):
#     if int(numbers[i]) - 1 != int(numbers[i - 1]):
#         print(int(numbers[i - 1]) + 1)

list = [numbers[i - 1] + 1 for i in range(1, len(numbers)) if numbers[i] - 1 != numbers[i - 1]]
print(list[0])