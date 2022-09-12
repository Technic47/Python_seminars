# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python


def solution(a, b, c):
    desc = (b ** 2) - (4 * a * c)
    desc = desc ** 0.5
    if desc > 0:
        answer1 = (-b - desc) / (2 * a)
        answer2 = (-b + desc) / (2 * a)
        return answer1, answer2
    elif desc == 0:
        answer = (-b / (2 * a))
        return answer
    else:
        print('Wrong input')


a = 1
b = 17
c = -18
print(f'Your solution is: {solution(a, b, c)}')
