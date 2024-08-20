def solution(N, stages):
    answer = []
    surviver_cnt = len(stages)
    cnt_dict = {}
    failure_arr = []
    
    # 카운트 딕셔너리
    for stage in stages:
        cnt_dict[stage] = cnt_dict.get(stage, 0) + 1

    stages.sort()

    for current_stage in range(1, N + 1):
        if surviver_cnt > 0:
            failure_cnt = cnt_dict.get(current_stage, 0)
            failure_rate = failure_cnt / surviver_cnt
            failure_arr.append((failure_rate, current_stage))
            surviver_cnt -= failure_cnt
        else:
            failure_arr.append((0, current_stage))
    
    failure_arr.sort(key=lambda x : (-x[0], x[1])) # 조건에 맞춰 정렬
    
    for x in failure_arr:
        answer.append(x[1])
    
    return answer