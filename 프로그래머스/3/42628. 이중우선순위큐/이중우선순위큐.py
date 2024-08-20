# 문제 분석
# 최대 힙, 최소 힙 출력

# 접근
# [16, -5643, 123, -1]
# [-45, 163, 1, -642, 45, 97, 1, -1, 333]
# 최소 힙? 쉽다. 기본적으로 가능하다.
# 최대 힙? 쉽다. 원소에 음수를 곱해서 삽입하면 된다. 꺼낼 때 음수를 곱해서 꺼내고.
# 이중? 힙 구조를 그렇게 짤 수가 있을까? 부모가 언제나 크면서 작은 것은 불가능하다.
    # 부모를 튜플로 구성하거나
    # 최대힙, 최소힙을 동시에 짜거나
        # 이렇게 하자
        # insert는 cnt += 1
        # delete는 cnt -= 1
        # 연산을 해야 하는데 cnt < 0인 경우 return [0, 0]
        # 배열을 다 돌면 return [최댓값, 최소값]

import heapq
        
def solution(operations):
    answer = []
    minHeap = []
    maxHeap = []
    cnt = 0
    
    for oper in operations:
        if cnt == 0:
            minHeap = []
            maxHeap = []
        
        op, num = oper.split()
        
        if op == "I":
            heapq.heappush(minHeap, int(num))
            heapq.heappush(maxHeap, -int(num))
            cnt += 1
            
        elif cnt > 0:
            cnt -= 1
            if num == "1":
                heapq.heappop(maxHeap)
            else:
                heapq.heappop(minHeap)
    
    if cnt <= 0:
        return [0, 0]
    else:
        return [-heapq.heappop(maxHeap), heapq.heappop(minHeap)]

