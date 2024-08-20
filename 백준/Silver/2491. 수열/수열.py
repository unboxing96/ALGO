n = int(input())
arr = list(map(int, input().split()))

max_len = 1
increase_len = 1
decrease_len = 1

for i in range(1, n):
    if arr[i] >= arr[i - 1]:
        increase_len += 1
    else:
        increase_len = 1

    if arr[i] <= arr[i - 1]:
        decrease_len += 1
    else:
        decrease_len = 1

    max_len = max(max_len, increase_len, decrease_len)

print(max_len)
