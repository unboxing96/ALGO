# 이해
# 배열의 각 원소가 오름차순이 지속되는 길이를 각각 return
# 다음 원소와 비교하여, 값이 작아지지 않을 때마다 += 1
# 일단 지속 시간을 1초 증가시키고, 그 뒤에 오름차순 여부를 판단한다.
# 마지막 원소는 0초이다.

# 풀이
# 일단 이중 반복문으로 풀자

from collections import deque

def solution(prices):
    answer = []
    queue = deque(prices)
    
    while queue:
        price = queue.popleft()
        sec = 0
        
        for q in queue:
            sec += 1
            if price > q:
                break
        
        answer.append(sec)
    
    return answer