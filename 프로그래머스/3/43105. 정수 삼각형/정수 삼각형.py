# 풀이
# DP로 누적합 배열을 만든다.
# 모서리과 가운데 케이스로 나누어 해결한다.
# 모서리는 위층에서 그대로 받는다.
# 가운데는 위층의 양쪽에서 큰 값을 받는다.

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j], triangle[i-1][j-1])
    
    answer = max(triangle[-1])
    return answer