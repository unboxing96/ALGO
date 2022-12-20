import sys

sys.stdin = open("2460.txt", "r")

# now = 현재 사람 수
# most = 가장 많은 사람 수
# 역에 도착하여, 내리고 탄 뒤에, most와 비교
# most보다 크면 교체

now = 0
most = 0

for tc in range(10):
    off, on = map(int, input().split())
    now -= off
    now += on
    if now > most:
        most = now

print(most)
