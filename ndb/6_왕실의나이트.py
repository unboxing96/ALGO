# 8 8 매트릭스 생성
# 나이트 방식으로 이동 후, 좌표값을 결과 리스트에 추가

# 체스판 벗어나면 pass
# abcdefgh를 순회하며, index 값으로 변환하는 과정 필요

start = input()

matrix = [[0] * 8 for _ in range(8)]

dx = [2, 2, -2, -2, 1, 1, -1, -1]
dy = [1, -1, 1, -1, 2, -2, 2, -2]

column = "abcdefgh"


x = column.index(start[0]) + 1
y = int(start[1])

cnt = 0
for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > 8 or ny > 8:
        continue
    else:
        cnt += 1

print(cnt)