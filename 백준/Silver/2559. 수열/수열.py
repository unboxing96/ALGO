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