N = int(input())

result = []

for num in range(4, N+1):
    isBool = True

    for i in str(num):
        if i not in "47":
            isBool = False
    
    if isBool:
        result.append(num)

print(max(result))