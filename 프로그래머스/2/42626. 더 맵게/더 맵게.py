# 이해
# 최소 힙
# 값이 작은 2개를 pop()해서, 특정 공식으로 계산된 결과를 push()
# 최소 값이 K를 넘을 때까지 반복

# 풀이
# scoville = heapq.heapify(scoville)
# cnt = 0
# while True:
    # scoville을 정렬하여, [0]번째 원소가 K보다 작으면 (heap은 subscription이 가능한가?)
        # first = heapq.heappop(scoville)
        # second = heapq.heappop(scoville)
        # new = first + (second * 2)
        # heapq.heappush(scoville, new)
        # cnt += 1
    # 작지 않으면 return cnt
    

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while len(scoville) >= 2:
        if scoville[0] < K:
            first = heapq.heappop(scoville)
            second = heapq.heappop(scoville)
            new = first + (second * 2)
            heapq.heappush(scoville, new)
            answer += 1
        else:
            return answer
    
    return answer if scoville[0] >= K else -1
        
