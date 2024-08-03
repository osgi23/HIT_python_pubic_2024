n, m = input().split()
n = int(n)
m = int(m)

array = input().split()
array = [int(x) for x in array]

A = input().split()
A = set(int(x) for x in A)
B = input().split()
B = set(int(x) for x in B)

h = 0

for i in array:
    if i in A:
        h += 1
    elif i in B:
        h -= 1

print(h)
