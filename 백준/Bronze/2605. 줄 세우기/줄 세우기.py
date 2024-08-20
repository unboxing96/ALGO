n = int(input())
orders = list(map(int, input().split()))
students = []

for i in range(n):
    students.insert(i - orders[i], i + 1)

print(*students)