# 이해
# 전체 작업 소요 시간의 평균이 최소가 되도록
# 매번 가능한 작업 중 소요 시간이 작은 것을 먼저 수행한다.
    # 반례가 있다.
    # [[0, 3], [4, 10], [5, 1], [6, 1]]
    # 3, 13, 14, 15 == 11.25
    # 3, 6, 7, 17 == 8.25
# 끝나는 시간을 기준으로 해야 할 듯하다.
# 배열을 탐색하여, 원소 별로 끝나는 시간(시작 시간 + 소요 시간)을 구한다.
# 끝나는 시간이 빠른 것 순서대로 처리한다.

# 풀이
# sorted_jobs = sorted(jobs, key= lambda x: x[0] + x[1])
# end_time_of_jobs = list(map(lambda x: x[0] + x[1], jobs))

import heapq

def solution(jobs):
    # 작업을 요청 시간 기준으로 정렬
    jobs.sort()
    
    # 현재 시간, 전체 작업 수, 대기 시간 총합
    now = 0
    total_jobs = len(jobs)
    total_waiting_time = 0
    
    # 처리할 작업들을 관리할 우선순위 큐
    ready_queue = []
    
    # jobs 인덱스
    index = 0
    
    while index < total_jobs or ready_queue:
        # 현재 시간 이하에 요청된 모든 작업을 ready_queue에 추가
        while index < total_jobs and jobs[index][0] <= now:
            heapq.heappush(ready_queue, (jobs[index][1], jobs[index][0]))
            index += 1
        
        if ready_queue:
            # 가장 짧은 작업을 처리
            duration, start_time = heapq.heappop(ready_queue)
            now += duration
            total_waiting_time += now - start_time
        else:
            # 대기 중인 작업이 없다면 현재 시간을 다음 작업의 요청 시간으로 이동
            now = jobs[index][0]
    
    # 평균 대기 시간 계산 후 반환
    return total_waiting_time // total_jobs



