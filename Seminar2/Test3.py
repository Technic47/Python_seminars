# Для натурального n создать последовательности 3n + 1.

number = int(input('Enter your number: '))

for i in range(1, number + 1):
    num = (3 * i + 1)
    print(f"{i}: {num}")
