import sys
sys.stdin = open("2527.txt")

# 문제 분석
# (x, y) (p, q) 순서로 주어진다.
# 좌표 값의 범위가 50,000이므로 탐색하는 것이 아니라 수학으로 푸는 문제이다.
# 직사각형 -> a
# 선분 -> b
# 점 -> c
# 공통 없음 -> d


for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 만나지 않는 경우
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
        continue

    elif (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2):
        print('c')
        continue

    elif x1 == p2 or y1 == q2 or p1 == x2 or q1 == y2:
        print('b')
        continue

    else:
        print('a')