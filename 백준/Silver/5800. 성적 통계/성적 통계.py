K = int(input())
for i in range(K):
    
    num = list(map(int, input().split()))
    del num[0]
    num.sort()
    big = []
    print(f"Class {i + 1}")
    for k in range(len(num) - 1):
        result = int(num[k + 1] - num[k])
        big.append(result)
    print(f"Max {max(num)}, Min {min(num)}, Largest gap {max(big)}")