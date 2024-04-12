# 이해
# progresses의 원소는 100%를 달성하면 배포된다.
# 매일 speeds의 원소만큼 progress가 진행된다.
# 가장 앞에 있는 원소가 100%를 달성한 순간에, 100%를 달성한 모든 원소를 배포한다.

# 풀이
# progresses의 각 원소를 100에서 빼고, 그 값을 speeds로 나누어 남은 일자를 계산한다. remain_days: [Int]
# remain_days를 탐색하며, 내림차순으로 정렬된 경우 tmp에 더하고, 
    # 내림차순이 깨진 순간 tmp를 answer에 append하고, tmp를 초기화 한다.
# answer를 return한다.

import math

def solution(progresses, speeds):
    days_needed = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    result = []
    
    current_max_day = days_needed[0]
    count = 0
    
    for day in days_needed:
        if day <= current_max_day:
            count += 1
        else:
            result.append(count)
            current_max_day = day
            count = 1
            
    result.append(count)  # 마지막 배치를 추가
    return result
    
    return answer