# 이해
# 빈 공간에 "딱 맞는" 크기로 조각을 채워넣을 수 있음. 채워넣은 뒤에 공간이 남으면 안 됨.
# 조각은 회전 가능. 뒤집기 불가능.
# 최대한 많은 조각을 채울 경우, 빈 공간을 몇 칸이나 채울 수 있는지?
# 행렬 회전이 필요하네 ..

# 풀이
# game_board와 table에서 연결 요소의 인덱스 정보를 얻어야 한다.
# bfs() 함수로 연결 요소들의 인덱스 정보를 얻는다.
# find_table() 함수로 인덱스 정보를 (0, 0)을 기준으로 하는 2차원 행렬로 바꾼다.
# rotate() 함수로 배열을 회전한다. 하는 김에 연결 요소의 크기도 계산한다.

# solution()
# game_board를 bfs()로 탐색하여 인덱스 정보empty_boards를 얻는다.
# table을 bfs()로 탐색하여 인덱스 정보puzzles를 얻는다.

# for empty_board in empty_boards:
    # make_table() 함수로 empty_board를 2차원 행렬로 바꾼다.
    # for puzzle in puzzles:
        # make_table() 함수로 puzzle을 2차원 행렬로 바꾼다.
        # 4번 반복한다. 90도 회전은 4번 가능하니까.
            # empty_board와 회전한 puzzle이 같다면
                # answer에 연결 요소의 크기를 더한다.
                # puzzles에서 puzzle을 제거한다.
                # 탐색을 멈춘다.

from collections import deque
                
def solution(game_board, table):
    answer = 0
    
    empty_idx_set_list = bfs(game_board, 0)
    puzzle_idx_set_list = bfs(table, 1)
    
    # 사용한 퍼즐을 추적하기 위한 방법 변경
    used_puzzles = [False] * len(puzzle_idx_set_list)  # 퍼즐 사용 여부를 체크하기 위한 리스트
    
    for empty_idx_set in empty_idx_set_list:
        isFilled = False
        empty_table = find_table(empty_idx_set)
        
        for idx, puzzle_idx_set in enumerate(puzzle_idx_set_list):
            if used_puzzles[idx]:  # 이미 사용된 퍼즐은 건너뛴다
                continue
            
            if isFilled:
                break
            
            puzzle_table = find_table(puzzle_idx_set)
            
            for _ in range(4):
                puzzle_table, cnt = rotate(puzzle_table)
                if empty_table == puzzle_table:
                    answer += cnt
                    used_puzzles[idx] = True  # 퍼즐을 사용했다고 표시
                    isFilled = True
                    break
    
    return answer


def bfs(matrix, standard):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    empty_board_list = []
    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):  # matrix 길이 대신 matrix[0] 길이로 변경
            if matrix[i][j] == standard:
                matrix[i][j] = 1 - standard
                q = deque([(i, j)])
                tmp_list = [(i, j)]
                
                while q:
                    x, y = q.popleft()
                    
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        
                        if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]) and matrix[nx][ny] == standard:
                            matrix[nx][ny] = 1 - standard
                            q.append((nx, ny))
                            tmp_list.append((nx, ny))
                
                empty_board_list.append(tmp_list)
    
    return empty_board_list


def find_table(idx_list):
    x_list, y_list = zip(*idx_list)
    row = max(x_list) - min(x_list) + 1
    col = max(y_list) - min(y_list) + 1
    matrix = [[0] * col for _ in range(row)]
    
    for x, y in idx_list:
        matrix[x - min(x_list)][y - min(y_list)] = 1
    
    return matrix


def rotate(matrix):
    row, col = len(matrix), len(matrix[0])
    rotated_matrix = [[0] * row for _ in range(col)]
    cnt = 0
    
    for i in range(row):
        for j in range(col):
            rotated_matrix[j][row - 1 - i] = matrix[i][j]
            if matrix[i][j] == 1:
                cnt += 1
    
    return rotated_matrix, cnt
