m = int(input())
n = int(input())
arr = []
for i in range(m,n+1):
    count = 0
    for j in range(1,i):
        if i%j == 0:
            count+=1
        if count == 2:
            break
        if j == i-1:
            arr.append(i)

if arr:
    print(sum(arr))
    print(arr[0])
else:
    print(-1)