import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
questions = int(input())

# 전처리 -> 누적합
prefix = [0 for _ in range(n + 1)]
tmp = 0
for i in range(n - 1):
    if nums[i] > nums[i + 1]:
        tmp += 1
    prefix[i + 1] = tmp

prefix[-1] = tmp

# 답 찾기
for _ in range(questions):
    x, y = map(int, input().split())
    print(prefix[y - 1] - prefix[x - 1])