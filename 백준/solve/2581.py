a = int(input())
b = int(input())

sosu = []

for num in range(a, b+1):
    
    if num <= 1:
        continue

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        sosu.append(num)

if len(sosu) == 0:
    print(-1)

else:
    sosu.sort()

    print(sum(sosu))
    print(sosu[0])