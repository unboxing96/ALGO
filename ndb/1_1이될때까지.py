# N: 기준 수
# K: 계산하는 수

# 1. N을 K로 최대한 나눠준다
# 2. 나머지 만큼 빼준다

N, K = map(int, input().split())

div = N % K

cnt = 0

while True:
    N //= K
    if N == 0: break
    cnt += 1

print(cnt + div)

