# bai 3 - a
n = int(input())
tong = 0
for i in range(1, (2*n + 1) + 1, 1):
    if i % 2 != 0:
        tong += i
    else:
        tong -= i
print(tong)

# bai 3 - b
n2 = int(input())
tong2 = 0
for i in range(1, n2 + 1, 1):
    tong2 += 1 / i
print(tong2)

# bai 3 - c
a = float(input())
b = float(input())
c = float(input())
if a == b and b == c and c == 0:
    print("vo so nghiem")
if a == 0:
    if b == 0:
        print("vo nghiem")
    else:
        print(-c / b)
else:
    delta = b*b - 4*a*c
    if delta < 0:
        print("Vo nghiem")
    elif delta == 0:
        print(-b/(2*a))
    else:
        print("x1 = " + str((-b + delta**(1/2))/(2*a)))
        print("x2 = " + str((-b - delta**(1/2))/(2*a)))