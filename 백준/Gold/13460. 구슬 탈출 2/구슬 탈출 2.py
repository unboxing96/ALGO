from collections import deque

n, m = map(int, input().split())
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()


def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                rx, ry = i, j
            elif graph[i][j] == "B":
                bx, by = i, j
    # 0 is cnt
    q.append((rx, ry, bx, by, 0))
    # visited
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy, cnt):
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    return x, y, cnt


def bfs():

    while q:
        # pop queue which is started from init()
        rx, ry, bx, by, depth = q.popleft()

        # 1 issue
        if depth >= 10:
            break

        for i in range(4):
            # move() for each r and b
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i], 0)

            # if B == "O": continue
            if graph[nbx][nby] == "O":
                continue

            if graph[nrx][nry] == "O":
                print(depth + 1)
                return

            # R and B is arrived "#"
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                else:  # rcnt < bcnt:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            # visited check:
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))

    print(-1)


init()
bfs()
