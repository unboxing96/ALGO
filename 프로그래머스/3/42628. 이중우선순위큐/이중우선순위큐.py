# 이해
# 명령어를 받아서 힙을 구성
# 명령어에 따라 최솟값 혹은 최댓값을 pop()
# 모든 명령어를 수행하고 남은 힙의 최솟값과 최댓값을 return

# 풀이
# 명령어의 순서를 미리 기록한다.
# 가령 최솟값 삭제면 False, 최댓값 삭제면 True
# 힙에 추가하는 명령어를 실행할 때마다, 순서 배열을 보면서 최댓값 삭제(True)인 경우 -값을 추가한다.
# 모든 명령어는 최솟값 삭제로 실행한다.

# 풀이2
# O(NlogN) 풀이가 떠오르지 않아서 구글링을 했다.
# 다들 그냥 remove 함수를 사용한다.
# O(N^2) 아닌가...? N == 10 ** 6이니까 10 ** 12로, 시간 초과 기준(10 ** 9)을 아득히 넘는다.
# 완성된 힙을 탐색하는 것이 아니라, 완성해가면서 탐색하는 것이기 때문에 가능한가보다.
# 다시 한번 느꼈다. 프로그래머스에서 문제 풀 때는 시간 복잡도는 신경 쓰는 것이 아니다.
# N이 1억이나 10억이면 이분 탐색 문제이고, 아니라면 일단 O(N ** 2)으로 풀이하자.

import heapq

def solution(operations):
    answer = []
    heap = []
    
    for operation in operations:
        op, num = operation.split()
        
        if op == "I":
            heapq.heappush(heap, int(num))
        elif heap:
            if num == "-1":
                heapq.heappop(heap)
            else: # num == "1"
                heap.remove(max(heap))
    
    return [0, 0] if len(heap) == 0 else [max(heap), min(heap)]











