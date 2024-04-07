# 풀이
# lost 탐색하면서, -1, +1 값이 reserve에 있는지 확인한다.
# 있으면 lost, reserve에서 popleft 한다.
# 탐색이 끝나면 n - len(lost)

def solution(n, lost, reserve):
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)
    
    return n - len(set_lost)