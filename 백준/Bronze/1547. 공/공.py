ball = [[0], [1], [0], [0]]

T = int(input())

for tc in range(T):
    a, b = map(int, input().split())

    if ball[a][0] == 1:
        ball[a][0] -= 1
        ball[b][0] += 1
    
    elif ball[b][0] == 1:
        ball[b][0] -= 1
        ball[a][0] += 1
    
if ball.index([1]):
    print(ball.index([1]))
else:
    print(-1)