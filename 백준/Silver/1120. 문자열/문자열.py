a, b = input().split()
min_diff = 10000

for i in range(len(b)-len(a)+1):
    diff = 0

    for j in range(len(a)):
        if a[j] != b[j+i]:
            diff += 1

    if diff < min_diff:
        min_diff = diff
    
print(min_diff)
