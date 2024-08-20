# 문제 분석
# 빙고
# 사회자 불러주는 값을 하나씩 방문 처리한다.
# 방문 처리할 때마다 가로, 세로, 대각선 방향의 빙고를 점검한다.
# 3번째 빙고를 하는 순간, 몇 번째 도전 차수였는지 return 한다.


# 접근
# 빙고를 점검하는 함수를 구현한다.
    # 가로 방향
        # 현재 위치와 x는 같고, y가 0 ~ n-1까지
    # 세로 방향
        # 현재 위치와 y는 같고, x가 0 ~ n-1까지
    # 양 대각선 방향
        # 전체 배열에서 i == j인 경우와, i + j == 5 - 1인 경우
# 사회자가 숫자를 불러줄 때마다, 철수의 빙고판을 탐색하며 방문 처리한다.
    # 방문 처리는 그 값을 -1로 바꾸는 것으로 하자.
# bingo 카운트, stage 카운트 변수를 생성하여, bingo가 3이 되는 순간 stage를 return 한다.

import sys
sys.stdin = open("2578.txt")


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