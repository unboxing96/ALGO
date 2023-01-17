
from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[[[False] * m for _ in range(n)] for _ in range(m)] for _ in range(n)]
path = [
    [[[[0, 0, 0, 0, 0] for _ in range(m)] for _ in range(n)] for _ in range(m)]
    for _ in range(n)
]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
dir = ["U", "D", "L", "R"]
q = deque()


def init():
    rx, ry, bx, by = 0, 0, 0, 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == "R":
                rx, ry = i, j
            elif graph[i][j] == "B":
                bx, by = i, j
    # exit for loop
    # 0 is for depth
    q.append((rx, ry, bx, by, 0))
    # the first visit
    visited[rx][ry][bx][by] = True


def move(x, y, dx, dy, cnt):
    while graph[x + dx][y + dy] != "#" and graph[x][y] != "O":
        x += dx
        y += dy
        cnt += 1
    # exit while loop
    return x, y, cnt


def bfs():

    while q:
        rx, ry, bx, by, depth = q.popleft()

        if depth >= 10:
            break

        for i in range(4):
            nrx, nry, rcnt = move(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bcnt = move(bx, by, dx[i], dy[i], 0)

            # if B is arrived at HOLE
            if graph[nbx][nby] == "O":
                continue

            # if R is arrived at HOLE
            if graph[nrx][nry] == "O":

                p = []
                p.append(dir[i])

                mrx, mry, mbx, mby = rx, ry, bx, by
                while mrx:
                    mrx, mry, mbx, mby, k = path[mrx][mry][mbx][mby]
                    p.append(dir[k])
                p.pop()
                print(depth + 1)
                print(*p[::-1], sep="")
                return

            # when R and B are in same index
            if nrx == nbx and nry == nby:
                if rcnt > bcnt:
                    nrx, nry = nrx - dx[i], nry - dy[i]
                elif bcnt > rcnt:
                    nbx, nby = nbx - dx[i], nby - dy[i]

            # when first loop of for get done, check visited list
            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = True
                q.append((nrx, nry, nbx, nby, depth + 1))
                path[nrx][nry][nbx][nby] = (rx, ry, bx, by, i)

    # exit while loop, but R is cannot goal in
    print(-1)


init()
bfs()
