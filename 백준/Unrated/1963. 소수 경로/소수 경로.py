
import sys
from collections import deque
input = sys.stdin.readline

def findPrime():
    for i in range(2, 100):
        if prime[i] == True:
            for j in range(2 * i, 10000, i):
                prime[j] = False

def bfs():
    q = deque()
    q.append((start, 0))
    
    visited = [False for i in range(10000)]
    visited[start] = True

    while q:
        now, cnt = q.popleft()

        if now == end:
            return cnt

        strNow = str(now)

        for i in range(4):
            for j in range(10):
                temp = int(strNow[:i] + str(j) + strNow[i + 1:])

                if prime[temp] and not visited[temp] and temp >= 1000:
                    visited[temp] = True
                    q.append((temp, cnt + 1))

t = int(input())
prime = [True for i in range(10000)]
findPrime()

for _ in range(t):
    start, end = map(int, input().split())
    result = bfs()
    print(result if result != None else "Impossible")    
        