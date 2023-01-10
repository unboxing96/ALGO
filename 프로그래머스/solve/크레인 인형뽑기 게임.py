# x,y = y,x 좌표의 새로운 board 만들기
# moves를 순회하며, 0이 아닌 값을 만나면, 0으로 만들고,
# stack에 해당 값 추가할 때, 직전 값이 동일하면 쌓지 않고 result += 2, 동일하지 않으면 쌓음

from pprint import pprint

board = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 3],
    [0, 2, 5, 0, 1],
    [4, 2, 4, 4, 2],
    [3, 5, 1, 3, 1],
]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
stack = []
result = 0

n = len(board)

new = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        new[i][j] = board[j][i]

for i in range(len(moves)):  # moves 순회
    the = new[moves[i] - 1]
    for j in range(len(the)):  # moves 첫번째 요소에 해당하는, new의 행 순회
        if the[j] > 0:
            if stack and stack[-1] == the[j]:
                stack.pop()
                result += 2
                the[j] = 0
                break
            else:
                stack.append(the[j])
                the[j] = 0
                break

print(result)
