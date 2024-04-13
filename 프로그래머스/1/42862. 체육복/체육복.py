# 이해
# lost 도난 번호 체육복
# reserve 여분 체육복
# reserve는 양 옆 번호에만 빌려줄 수 있다
# reserve도 도난 당했을 수 있다.
# 체육 수업을 들을 수 있는 학생의 최댓값을 return

# 풀이
# 도난 당하고 남은 reserve를 구한다. set_reserve = set(reserve) - set(lost)
# 도난하고 남은 lost를 구한다. set_lost = set(reserve) - set(lost)
# (1, n+1)의 범위를 탐색하며, lost에 있는 값이라면, lost의 양 옆 범위를 탐색한다.
    # 양 옆에 범위에 reserve가 있으면 lost와 reserve에서 해당 원소를 삭제한다.
# 탐색이 종료되고, n - len(lost)를 출력한다.

def solution(n, lost, reserve):
    
    set_reserve = set(reserve) - set(lost)
    set_lost = set(lost) - set(reserve)
    
    for num in set_reserve:
        if num - 1 in set_lost:
            set_lost.remove(num - 1)
        elif num + 1 in set_lost:
            set_lost.remove(num + 1)
    
    return n - len(set_lost)




