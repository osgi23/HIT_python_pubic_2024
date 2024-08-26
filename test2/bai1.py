def sum_of_string(s):
    total, num = 0, ''
    for char in s:
        if char.isdigit() or (char == '-' and num == ''):
            num += char
        elif num:
            total += int(num)
            num = ''
    if num:
        total += int(num)
    return total

s = input()
result = sum_of_string(s)
print(result)