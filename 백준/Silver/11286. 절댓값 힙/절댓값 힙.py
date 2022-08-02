import heapq
import sys

N = int(input())

hq = []
heapq.heapify(hq)

for i in range(N):
    n = int(sys.stdin.readline())

    if n == 0: 
        if len(hq) == 0: 
            print(0) 
        else: 
            print(heapq.heappop(hq)[1])  
            
    elif n != 0:
        heapq.heappush(hq, (abs(n), n))