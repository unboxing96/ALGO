K = int(input())

result = []
for k in range(1, K+1):
    num = int(input())
    if num == 0:
        result.pop()
    else:
        result.append(num)

print(sum(result))