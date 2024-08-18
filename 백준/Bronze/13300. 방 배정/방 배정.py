n, k = map(int, input().split())
arr = [[0, 0] for _ in range(6 + 1)]
tot = 0

for _ in range(n):
    gender, grade = map(int, input().split())
    arr[grade][gender] += 1

for w, m in arr:
    tot += (w + k - 1) // k 
    tot += (m + k - 1) // k

print(tot)