# 문제 분석
# 1. 슬라이싱 i - 1 ..< j
# 2. 오름차순 정렬
# 3. k - 1 번째 숫자 return

def solution(array, commands):
    answer = []
    
    for com in commands:
        i, j, k = com[0], com[1], com[2]
        slicedArr = array[i - 1 : j]
        sortedArr = sorted(slicedArr)
        answer.append(sortedArr[k - 1])
    
    return answer