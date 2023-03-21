from collections import deque

tc = int(input())

for _ in range(tc):
    n = int(input())
    array = list(map(int, input().split()))
    array.sort(reverse=True)

    new_array = deque()
    for i in range(n):
        if i % 2 == 0:
            new_array.appendleft(array[i])
        else:
            new_array.append(array[i])
    
    biggest = 0
    for i in range(n-1):
        gap = abs(new_array[i] - new_array[i+1])
        if biggest < gap:
            biggest = gap
    
    print(biggest)