import sys

sys.stdin = open("input.txt", "r")


T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))

    result = sum(numbers) / len(numbers)

    result = round(result)

    print(f"#{i} {result}")