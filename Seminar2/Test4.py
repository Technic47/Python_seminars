# Напишите программу, в которой пользователь будет задавать две
# строки, а программа - определять количество вхождений одной строки в другой.


a = input("Введите строку: ")
b = input("Введите искомую подстроку: ")
# answer = a.count(b)  # build in finder
count = 0
for i in range(0, len(a) - len(b)):
    if b == a[i: i + len(b)]:
        count += 1

# print(answer)
print(f"{count} раз")
