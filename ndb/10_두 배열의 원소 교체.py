
import time
import sys
sys.stdin = open("10_두 배열의 원소 교체.txt", "r")

# 시작
start_time = time.time()


N, K = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()



for i in range(K):
    A[i], B[N-i-1] = B[N-i-1], A[i]

print(sum(A))



# 끝
end_time = time.time()
# 출력
print(end_time - start_time)