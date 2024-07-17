# Bai1 - a
i = int(input())
result = 0

while i > 0:
    result += i % 10
    i //= 10

print(result)

# Bai1 - b
n = int(input())
resultb = 0

for i in range(1, n + 1, 1):
    if n % i == 0:
        print(i)
        resultb += i

print(resultb)

# Bai1 - c
a = int(input())
b = int(input())
c = int(input())

if a <= 0 or b <= 0 or c <= 0:
    print("NO")
elif a + b <= c or b + c <= a or a + c <= b:
    print("NO")
elif a == b and b == c:
    print("DEU")
elif a == b or b == c or c == a:
    print("CAN")
elif a*a == b*b + c*c or b*b == a*a + c*c or c*c == b*b + a*a:
    print("VUONG")
elif a*a + b*b > c*c and a*a + c*c > b*b and b*b + c*c > a*a:
    print("NHON")
else:
    print("TU")
