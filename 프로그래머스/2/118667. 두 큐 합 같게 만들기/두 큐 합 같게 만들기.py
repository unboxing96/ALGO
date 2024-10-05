# 두 큐의 합이 같아야 한다.
    # 이때 합을 기준합이라고 하자.
# 두 큐의 합을 q1sum, q2sum으로 관리하며, 기준합보다 큰 곳에서 빼서, 기준합보다 작은 곳으로 더한다.
# 이동횟수가 큐 전체 길이를 넘을 경우 -1

from collections import deque

def solution(queue1, queue2):
    q1 = deque(queue1)
    q2 = deque(queue2)
    q1sum = sum(q1)
    q2sum = sum(q2)
    standard_sum = (q1sum + q2sum) // 2
    oper_cnt = 0
    
    while oper_cnt < 2 * (len(q1) + len(q2)):
        
        if q1sum == q2sum:
            break
        
        if q1sum > standard_sum:
            x1 = q1.popleft()
            q2.append(x1)
            q1sum -= x1
            q2sum += x1
        else:
            x2 = q2.popleft()
            q1.append(x2)
            q1sum += x2
            q2sum -= x2
        
        oper_cnt += 1
    

    return oper_cnt if oper_cnt < 2 * (len(q1) + len(q2)) else -1