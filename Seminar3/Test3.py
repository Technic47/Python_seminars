#  Напишите программу, которая определит позицию
#  второго вхождения строки в списке либо сообщит,
#  что её нет.


list1 = ["йцу", "фыв", "йцу", "фыв", "фыв", "фыв"]


if list1.count('йцу') <= 1:
     print('-1')
else:
     list1 = [i for i in range(len(list1)) if list1[i] == 'йцу' and list1[i] in list1]
     print(list1[1])