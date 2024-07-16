# 문제 분석
# 노란색 격자와 갈색 격자의 개수를 입력 받았을 때, 배열의 가로, 세로를 return
# 가로는 세로 길이 이상이다.

# 접근
# 갈색 격자의 개수는 노란색 격자와 상당히 상당한 상관이 있다.
# 노란 격자의 가로를 w, 세로를 h라고 하면, (w + 2) * (h * 2) <- 이것이 전체 개수이다.
# 노란 격자 개수의 1/2 범위 내에 약수를 구하고, 위 공식 == 노란 + 갈색일 때가 정답이다.

def solution(brown, yellow):
    
    for i in range(1, yellow + 1):
        if yellow % i == 0:
            w = i
            h = yellow // i
            nw = w + 2
            nh = h + 2
            size = brown + yellow

            if nw * nh == size:
                return [max(nw, nh), min(nw, nh)]