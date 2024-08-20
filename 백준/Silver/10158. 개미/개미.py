w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

# 개미의 위치는 2*w, 2*h마다 반복
cur_x = (p + t) % (2 * w)
cur_y = (q + t) % (2 * h)

# x 좌표
if cur_x > w:
    x = w - (cur_x - w) # 벽을 넘은 거리 cur_x - w -> # 전체 거리에서 넘은 만큼 빼기
else:
    x = cur_x

# y 좌표
if cur_y > h:
    y = h - (cur_y - h)
else:
    y = cur_y

print(x, y)
