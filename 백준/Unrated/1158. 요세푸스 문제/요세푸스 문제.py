import sys
input = sys.stdin.readline

n, k = map(int, input().split())
data = [i for i in range(1, n+1)]
answer = []

start = k - 1

for _ in range(n):
    if len(data) == 1:
        answer.append(data.pop())
        break

    answer.append(data.pop(start))    
    start = (start + k - 1) % len(data)


print(f"<{', '.join(map(str, answer))}>")