from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def bfs(board, dir):
    n = len(board)
    cost = [[int(1e9)] * n for _ in range(n)]
    cost[0][0] = 0

    q = deque()
    q.append((0, 0, 0, dir))  # row, col, cost, dir

    while q:
        x, y, c, d = q.popleft()

        if x == n - 1 and y == n - 1:
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            nd = i

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if board[nx][ny] == 1:
                continue

            if nd == d:
                nc = c + 100
            else:
                nc = c + 600

            if cost[nx][ny] > nc:
                cost[nx][ny] = nc
                q.append((nx, ny, nc, nd))

    return cost[-1][-1]


def solution(board):
    answer = min(bfs(board, 0), bfs(board, 2))
    return answer