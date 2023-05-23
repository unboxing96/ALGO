
n = int(input())
result = []
a = 2
b = 1

while True:
    
    tmp = a ** 2 - b ** 2

    if tmp < n:
        a += 1
    elif tmp > n:
        b += 1
    else:
        result.append(a)
        a += 1

    if a == b:
        break

if len(result) == 0:
    print(-1)
else:
    print(*result, sep = "\n")
