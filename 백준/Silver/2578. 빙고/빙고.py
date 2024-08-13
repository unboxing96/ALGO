chulsoo = [list(map(int, input().split() )) for _ in range(5)]
mc = [list(map(int, input().split() )) for _ in range(5)]
stage = 1
bingo = 0

def check_bingo():
    tmp_result = 0

    def check_bingo_horizontal():
        tmp_bingo = 0
        for i in range(5):
            tmp = 0
            for j in range(5):
                if chulsoo[i][j] == -1:
                    tmp += 1
                    if tmp == 5:
                        tmp_bingo += 1
        
        return tmp_bingo

    def check_bingo_sprial():
        tmp_bingo = 0
        for i in range(5):
            tmp = 0
            for j in range(5):
                if chulsoo[j][i] == -1:
                    tmp += 1
                    if tmp == 5:
                        tmp_bingo += 1
        
        return tmp_bingo
    
    def check_bingo_right_cross():
        tmp = 0
        for x, y in [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)]:
            if chulsoo[x][y] == -1:
                tmp += 1
                if tmp == 5:
                    return 1
        return 0
    
    def check_bingo_left_cross():
        tmp = 0
        for x, y in [(4, 0), (3, 1), (2, 2), (1, 3), (0, 4)]:
            if chulsoo[x][y] == -1:
                tmp += 1
                if tmp == 5:
                    return 1
        return 0

    
    tmp_result += check_bingo_horizontal()
    tmp_result += check_bingo_sprial()
    tmp_result += check_bingo_right_cross()
    tmp_result += check_bingo_left_cross()


    return tmp_result
    
    


def solution(stage, bingo):
    for m in range(25):
        mi = m // 5
        mj = m % 5
        current_stage_num = mc[mi][mj]

        for i in range(5):
            for j in range(5):
                if current_stage_num == chulsoo[i][j]:
                    chulsoo[i][j] = -1 # 방문 처리
                    if check_bingo() >= 3:
                        return stage

        stage += 1

result = solution(stage, bingo)
print(result)