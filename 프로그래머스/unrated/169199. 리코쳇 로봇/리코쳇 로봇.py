from collections import deque

def solution(board):
    rows, cols = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]  # 상, 하, 좌, 우

    # 로봇 위치(R)와 목표 위치(G) 찾기
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == "R":
                start = (i, j)
            if board[i][j] == "G":
                target = (i, j)

    visited = [[False] * cols for _ in range(rows)]
    queue = deque([(start, 0)])

    while queue:
        (row, col), moves = queue.popleft()
        # 목표 위치에 도달한 경우
        if (row, col) == target:
            return moves
        
        for dr, dc in directions:
            n_row, n_col = row, col
            while 0 <= n_row + dr < rows and 0 <= n_col + dc < cols and board[n_row + dr][n_col + dc] != "D":
                n_row += dr
                n_col += dc

            if (n_row, n_col) != (row, col) and not visited[n_row][n_col]:
                visited[n_row][n_col] = True
                queue.append(((n_row, n_col), moves + 1))

    # 목표 위치에 도달할 수 없는 경우
    return -1
