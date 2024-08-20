import sys
sys.stdin = open("13300.txt")

# 문제 분석
# 학년 개수 크기 + 1의 배열을 생성한다.
# 배열의 각 원소는 [여학생 수, 남학생 수] 형태로 저장한다.
# 입력을 받으면 카운트한다.
# 전체를 탐색하며 k개 나눈 몫과 나머지을 더한다.

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