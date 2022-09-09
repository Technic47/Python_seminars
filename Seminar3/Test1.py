#  Реализуйте алгоритм задания случайных чисел
#  без использования встроенного генератора псевдослучайных чисел.

import random
import datetime

number = int(input('Enter your number: '))

indexs = []
for i in range(number):
    index = random.randint(0, number - 1)
    if index in indexs:
        while index in indexs:
            index = random.randint(0, number - 1)
    indexs.append(index)

print(f"{indexs} - Selfmade random")


x = datetime.datetime.now()
rand_num = int(x.strftime("%f")) % 100
print(f"{rand_num} - DateTime random")
