# 이해
# yellow, brown 값을 보고 2차원 배열의 형태를 [가로, 세로]로 return

# 풀이
# brown은 언제나 (yellow_가로 + 2) * 2 + (yellow_세로) * 2 이다.
# yellow의 형태를 (1, 24), (2, 12), (3, 8), (4, 6) 순서로 바꿔가며 brown이 입력값과 일치하는지 판단.

# 의사코드
# 가로 i: 1부터 yellow의 제곱근 보다 작은 정수의 범위까지 탐색
# 세로: yellow // i
# yellow의 가로와 세로 길이로 brown의 값을 구한 뒤에 일치할 때까지 진행.
# 일치하면 [yellow_가로 + 2, yellow_세로 + 2] return

def solution(brown, yellow):
    
    for i in range(1, int(yellow ** 0.5) + 1):
        if yellow % i == 0:
            y_w = i
            y_h = yellow // i
        
        if brown == ((y_w + 2) * 2 + y_h * 2):
            b_w = max(y_w, y_h) + 2
            b_h = min(y_w, y_h) + 2        
            return [b_w, b_h]



