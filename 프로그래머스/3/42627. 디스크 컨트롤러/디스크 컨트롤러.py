# 이해 1
# 전체 작업 소요 시간의 평균이 최소가 되도록
# 매번 가능한 작업 중 소요 시간이 작은 것을 먼저 수행한다.
    # 반례가 있다.
    # [[0, 3], [4, 10], [5, 1], [6, 1]]
    # 3, 14, 15, 16 == 11.25
        # 3 + 10 + 10 + 10
    # 3, 6, 7, 17 == 8.25
        # 3, 1, 1, 10
# 끝나는 시간을 기준으로 해야 할 듯하다.
# 배열을 탐색하여, 원소 별로 끝나는 시간(시작 시간 + 소요 시간)을 구한다.
# 끝나는 시간이 빠른 것 순서대로 처리한다.

# 이해2
# 이해 1은 틀렸다 !! 정확히는 문제의 조건에 부합하지 않는다.
# <제한사항>의 마지막 항목: "하드디스크가 작업을 수행하고 있지 않을 때에는 먼저 요청이 들어온 작업부터 처리합니다."
# 따라서 수행 가능한 작업이 있다면 즉시 실행한다.
# 수행 가능한 작업이 여러 개가 있다면 소요 시간이 짧은 것을 실행한다.

# 풀이
# 현재 시간을 표시할 변수 now = 0
# 총 대기 시간 변수 total_waiting_time = 0
# 현재 가능한 작업 큐 ready_queue = []
# 현재 index = 0

# while ready_queue or index < len(jobs):
    # while now <= jobs[index][0]: # 현재 시간 now보다 작은(실행 가능한) 작업 모두 추가
        # ready_queue에 추가 (소요 시간, 시작 시간)
        # index += 1
    
    # if ready_queue:
        # duration, start = heappop()
        # now += duration
        # total_wating_time = now - start
    # else:
        # now = jobs[index][0]
        

# return total_wating_time // len(jobs)
    
    




import heapq

def solution(jobs):
    jobs.sort()
    now = 0
    total_waiting_time = 0
    index = 0
    ready_queue = []

    while index < len(jobs) or ready_queue:
        while index < len(jobs) and jobs[index][0] <= now: # 현재 시간 now보다 작은(실행 가능한) 작업 모두 추가
            heapq.heappush(ready_queue, (jobs[index][1], jobs[index][0]))
            index += 1

        if ready_queue:
            duration, start = heapq.heappop(ready_queue)
            now += duration
            total_waiting_time += now - start
        else:
            now = jobs[index][0]

    return total_waiting_time // len(jobs)



