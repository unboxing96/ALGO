# 첫 번째 선택
# 첫+1 번째 제외
# (n // 2) + (n % 2) = 최대 선택 가능 개수
# 

n = int(input())
array = list(map(int, input().split()))

# DP 테이블 초기화
d = [0] * 100

# DP 진행 (바텀업)
d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d[n-1])