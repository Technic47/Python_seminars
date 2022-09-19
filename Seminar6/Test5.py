a = "555+55*55-66/5"

num_list = []

num = ''
for char in a:
    if char.isdigit():
        num = num + char
    else:
        if num != '':
            num_list.append(int(num))
            num = ''
            num_list.append(char)
if num != '':
    num_list.append(int(num))

print(num_list)
