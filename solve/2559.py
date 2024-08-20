import sys
sys.stdin = open("2559.txt")

# 문제 분석
# 연속한 K일의 합 중에서 가장 큰 값을 return

# 접근
# 누적합 배열을 n + 1 크기로 구한다.
# 0..<n + 1 - k 범위를 탐색하며 부분합이 최대가 되는 구간을 찾는다. 이때 합을 return 한다.

n, k = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열
count_arr = [0] * (len(arr) + 1)
for i in range(1, len(count_arr)):
    count_arr[i] = count_arr[i - 1] + arr[i - 1]

# 부분합 최대
max_sum = -1e7 - 1

for i in range(n + 1 - k):
    tmp_sum = count_arr[i + k] - count_arr[i]
    max_sum = max(max_sum, tmp_sum)

print(max_sum)