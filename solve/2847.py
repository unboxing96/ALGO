n = int(input())
array = []
for _ in range(n):
    array.append(int(input()))

count = 0
for i in range(n-1, 0, -1):
    if array[i] <= array[i-1]:
        count += (array[i-1] - array[i] + 1)
        array[i-1] = array[i] - 1

print(count)
