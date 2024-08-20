# 문제 분석
# scoville의 모든 요소가 K 이상이 되도록 "섞기" 진행
# 조건을 만족했을 때까지의 "섞기" 횟수를 return
# 조건을 만족할 수 없으면 -1 return

# 접근
# mixCount = 0 # 섞기 횟수
# scoville에서 최소 값을 pop()
    # 해당 값이 K 이상이면 mixCount를 return
    # 해당 값이 K보다 작으면 추가로 pop()
        # 2개의 값을 섞는다. a + (b * 2)
        # 섞은 값을 scoville에 추가한다.
# scoville의 원소가 더 이상 남아 있지 않다면, -1을 return 한다.

import heapq

def solution(scoville, K):
    mixCount = 0
    heapq.heapify(scoville)
    
    while scoville:
        firstElement = heapq.heappop(scoville)
        
        if firstElement >= K:
            return mixCount
        else:
            if not scoville:
                return -1
            
            mixCount += 1
            secondElement = heapq.heappop(scoville)
            mixedElement = firstElement + (secondElement * 2)
            heapq.heappush(scoville, mixedElement)
    
    return -1







