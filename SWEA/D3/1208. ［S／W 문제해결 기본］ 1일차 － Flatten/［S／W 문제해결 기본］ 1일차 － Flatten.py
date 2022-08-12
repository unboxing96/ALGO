for t in range(1, 11):
    dump = int(input())
    height = list(map(int, input().split()))

    for i in range(dump):
        height[height.index(min(height))] += 1
        height[height.index(max(height))] -= 1

    print(f"#{t}", max(height) - min(height))