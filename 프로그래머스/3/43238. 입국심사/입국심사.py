# 이해
# 여러 개의 심사대에 심사관이 한 명씩 있다
# 각 심사관의 소요 시간은 다르다
# 대기하는 사람은 비어있는 심사대에서 심사를 받을 수 있다
# 혹은 기다렸다가 갈 수도 있다. 즉시 가지 않아도 된다는 뜻 ?
# 모든 심사를 완료하는 최소 시간을 return
# n은 심사를 기다리는 사람 수
# times는 각 심사위원의 속도

# 풀이
# 이분탐색
# 피봇의 범위와, 판단 기준을 선택해야 한다.
# 피봇의 범위는 총 소요 시간으로 해야겠다.
# 총 소요 시간을 times의 각 원소로 나누면, 해당 시간 내 심사관이 처리 가능한 인원 수가 나온다.
# 이 인원 수를 판단 기준으로 한다.

# Dr.code
# left = 1
# right = max(times) * n
# while left <= right:
    # mid = (left + right) // 2
    # people = 0
    # for time in times:
        # people += mid // time

def solution(n, times):
    answer = int(1e9)
    left = 1
    right = max(times) * n
    
    while left <= right:
        mid = (left + right) // 2
        people = 0
        for time in times:
            people += mid // time
    
        if people >= n:
            answer = mid
            right = mid - 1

        else: # people < n:
            left = mid + 1
        
    return answer







