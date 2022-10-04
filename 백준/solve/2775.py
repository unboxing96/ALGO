tc = int(input())

for _ in range(tc):
    k = int(input())  # 층
    n = int(input())  # 호
    floor = [i + 1 for i in range(n + 1)]
    for i in range(k):
        for j in range(1, n + 1):
            floor[j] += floor[j - 1]

    print(floor[-2])
