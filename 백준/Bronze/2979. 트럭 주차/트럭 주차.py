a, b, c = map(int, input().split())

arr = [0]*100
answer = 0

for _ in range(3):
    begin, end = map(int, input().split())
    for i in range(begin, end): 
        arr[i] += 1

for j in arr:
    answer += {0:0, 1:a, 2:b*2, 3:c*3}[j]

print(answer)