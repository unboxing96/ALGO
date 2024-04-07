# 이해
# 모든 심사대 비어있음
# 한 심사대 동시에 한 명만

# 풀이
# 피봇 포인터는 시간이다.
# 포인터를 움직이며 n을 달성할 수 있는지를 기준으로 판단하자.

def solution(n, times):
    
    answer = 0
    l = 1
    r = max(times) * n
    
    while l <= r:
        people = 0
        mid = (l + r) // 2
        
        for time in times:
            people += mid // time
            
            if people >= n:
                break
        
        if people >= n:
            answer = mid
            r = mid - 1
        else:
            l = mid + 1
            
    return answer