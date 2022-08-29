# 정수 N이 입력
# 00:00:00부터 N:59:59까지 3이 포함되는 경우의 수

# h, m, s 변수 생성
# s += 1을 무한 반복하며, 3이 있으면 cnt
# s = 60이 되면, m += 1, s = 0
# m = 60이 되면, h += 1, m = 0
# 정해진 시각이 되면 break

N = int(input())

cnt = 0

for h in range(N + 1):
    for m in range(60):
        for s in range(60):
            if "3" in str(h) + str(m) + str(s):
                cnt += 1

print(cnt)