str = {}
s = input()

for i in s:
    if i in str:
        str[i] += 1
    else:
        str[i] = 1
print(str)