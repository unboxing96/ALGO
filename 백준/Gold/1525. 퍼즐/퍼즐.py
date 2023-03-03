from collections import deque

# 2차원 행렬을 문자열로 바꿔서 판단
puzzle = ""
for _ in range(3):
    puzzle += "".join(list(input().split()))

# 그리고 해당 문자열을 key로, 이동 횟수를 value로 하는 딕셔너리 생성
dist = {puzzle: 0}
q = deque([puzzle])

# 델타 좌표
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    while q:
        puzzle = q.popleft()
        z = puzzle.index("0")

        if puzzle == "123456780":
            return dist[puzzle]

        x = z // 3
        y = z % 3

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 3 and 0 <= ny < 3:
                nz = nx * 3 + ny
                puzzle_list = list(puzzle)
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]
                new_puzzle = "".join(puzzle_list)

                if dist.get(new_puzzle, 0) == 0:
                    dist[new_puzzle] = dist[puzzle] + 1
                    q.append(new_puzzle)
    return -1


print(bfs())