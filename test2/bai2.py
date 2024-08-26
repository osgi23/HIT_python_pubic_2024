def perfect_number(k):
    count = 0
    num = 19  
    while True:
        if sum(int(digit) for digit in str(num)) == 10:
            count += 1
            if count == k:
                return num
        num += 9
k = int(input())
result = perfect_number(k)
print(result)