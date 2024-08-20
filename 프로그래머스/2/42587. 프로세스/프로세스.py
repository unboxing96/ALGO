# 문제 분석
# priorities 배열은 우선순위(원소의 값은 큰 순서)대로 제거해야 한다.
# 일종의 원형 큐처럼 동작한다.
# 현재 배열에서 가장 우선 순위가 높은 원소를 만날 때까지, 앞에서 제거 및 뒤에 추가를 반복한다.
# location 위치의 원소가 실행되는 순서를 구하라. (위치는 0부터, 순서는 1부터)

# 접근
# priorities 배열을 탐색하면서, [priority, index] 형태의 priorityWithIndex 배열을 생성한다.
# priorities 배열을 오름차순 정렬한 sortedPriorities 배열을 생성한다.
# while priorityWithIndex:
    # top = priorityWithIndex.popleft()
    # if top[0] == sortedPriorities[-1]: # 정상 실행
        # cnt += 1
        # sortedPriorities.pop()
        # if top[1] == location:
            # return cnt
    # else: # 다시 큐에 삽입
        # priorityWithIndex.append(top)

from collections import deque
    
def solution(priorities, location):
    
    cnt = 0
    
    priorityWithIndex = deque()
    for i in range(len(priorities)):
        priorityWithIndex.append([priorities[i], i])
        
    sortedPriorities = sorted(priorities)
    
    while priorityWithIndex:
        top = priorityWithIndex.popleft() # top = [priority, index]
        if top[0] == sortedPriorities[-1]: # 정상 실행
            cnt += 1
            sortedPriorities.pop()
            if top[1] == location:
                return cnt
        else: # 다시 큐에 삽입
            priorityWithIndex.append(top)