#  \\C:\Users\Pavel\Documents\GeekBrain\Python\Seminar4\Test_file

# 1. Задайте строку из набора чисел. Напишите программу, которая покажет
# большее и меньшее число. В качестве символа-разделителя используйте пробел.


def list_add(ourstr):
    numbers = []
    for item in ourstr:
        numbers.append(int(item))
    return numbers


ourstr = input('Enter your strings via space').split(' ')
numbers = list_add(ourstr)
print(numbers)
print(f'Your min value is: {min(numbers)};\nYour max value is: {max(numbers)}')
