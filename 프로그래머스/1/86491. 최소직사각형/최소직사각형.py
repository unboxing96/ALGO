# 문제 분석
# 길이가 2인 배열이 여러 개 주어진다. 한 쪽은 가로, 한 쪽은 세로이다.
# 모든 가로와, 모든 세로의 각각의 최댓값을 구하라

# 접근
# 2개의 원소를 입력받으면, 큰 것을 maxNum에, 작은 것을 minNum에 기존 값과 비교하여 할당한다.
# 배열 탐색을 종료하고 maxNum * minNum을 return한다.

def solution(sizes):
    answer = 0
    maxNum = 0
    minNum = 0
    
    for size in sizes:
        bigNum, smallNum = map(int, size)
        if bigNum < smallNum:
            bigNum, smallNum = smallNum, bigNum
        
        maxNum = max(maxNum, bigNum)
        minNum = max(minNum, smallNum)
    
    answer = maxNum * minNum
    
    return answer