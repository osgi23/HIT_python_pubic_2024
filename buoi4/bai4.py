n = int(input())
s = input().split()
s = set(int(x) for x in s)
m = int(input())

s_tmp = set()
lst = sorted(s)
sum = 0
for i in lst:
    sum += i
    if sum > m:
        break
    s_tmp.add(i)

print(s_tmp)
