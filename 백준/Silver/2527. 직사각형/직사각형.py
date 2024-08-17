for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 만나지 않는 경우
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print('d')
        continue

    elif (x1 == p2 and y1 == q2) or (x1 == p2 and q1 == y2) or (p1 == x2 and q1 == y2) or (p1 == x2 and y1 == q2):
        print('c')
        continue

    elif x1 == p2 or y1 == q2 or p1 == x2 or  q1 == y2:
        print('b')
        continue

    else:
        print('a')