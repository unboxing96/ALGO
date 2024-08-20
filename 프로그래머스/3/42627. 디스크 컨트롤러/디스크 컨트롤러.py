# 문제 분석
# jobs에 주어진 모든 작업의, 요청부터 종료까지 소요되는 시간의 평균이, 최소가 되도록 하라
# jobs의 요소는 [요청 시점, 소요 시간]

# 접근
# 어떤 조건에서 평균이 최소가 되는지 직관적으로는 모르겠다.
# 종료 시점(요청 시점 + 소요 시간)이 빠른 순서로 하면 될 것 같은 느낌은 있다.
# heapify 말고 직접 힙에 넣어주는 방식으로 heap을 생성한다.
    # 배열을 생성한다. 모든 원소를 heapq.heappush(배열, 인자)로 삽입한다.
        # 이때 인자를 (합, 요청 시점, 소요 시간으로 한다.)

# tot = 0
# while arr:
    # time += 1
    # now = heapq.heappop(arr)
    # if now[1] <= time: # 현재 시간이 요청 시점을 지나서, 실행이 가능한 상태
        # time += now[2] # 종료되는 시점
        # tot += time - now[1] # 총 소요 시간 (종료 시점 - 요청 시점)
    # else:
        # heapq.heappush(arr, now) # 실행이 불가능한 상태이면, 도로 배열에 삽입

# return tot / len(jobs)

import heapq

def solution(jobs):
    answer = 0
    last = -1 # 이전 작업의 종료 시점
    now = 0 # 현재 시점
    cnt = 0 # 처리한 작업의 개수
    h = []
    
    while cnt < len(jobs):
        for job in jobs:
            if last < job[0] <= now:
                heapq.heappush(h, (job[1], job[0]))
        
        if h:
            current = heapq.heappop(h)
            last = now
            now += current[0] # 완료 시각
            answer += now - current[1] # 요청 시각
            cnt += 1 # 완료한 작업 개수 추가
        else:
            now += 1 # 현재 시점 증가
    
    return answer // len(jobs)