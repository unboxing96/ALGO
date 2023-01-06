from pprint import pprint

# BFS
# 3방 델타 탐색
# 4블록 확인되면 0으로 바꾸고
# BFS 종료되면, 열행 그래프 돌면서 0은 빈 문자열로 replace
# 2~4 반복
# pop()한 개수 출력

# 파이썬
def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(n - 1):
        for j in range(m - 1):
            if b[i][j] == b[i + 1][j + 1] == b[i + 1][j] == b[i][j + 1] != "_":
                pop_set |= set([(i, j), (i + 1, j + 1), (i + 1, j), (i, j + 1)])
    # set_board
    for i, j in pop_set:
        b[i][j] = 0
    for i, row in enumerate(b):
        empty = ["_"] * row.count(0)
        b[i] = empty + [block for block in row if block != 0]
    return len(pop_set)


def solution(m, n, board):
    count = 0
    b = list(map(list, zip(*board)))
    while True:
        pop = pop_num(b, m, n)
        if pop == 0:
            return count
        count += pop


m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))
