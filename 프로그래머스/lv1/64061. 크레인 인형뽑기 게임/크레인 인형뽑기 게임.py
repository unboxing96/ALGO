def solution(board, moves):
    stack = []
    result = 0

    n = len(board)

    new = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            new[i][j] = board[j][i]

    for i in range(len(moves)):
        the = new[moves[i] - 1]
        for j in range(len(the)):  
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
    answer = result
    return answer