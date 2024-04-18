# 이해
# 출발 위치, 도착 위치
# rocks에는 바위 위치 배열
# rocks에서 n개를 제거
# 출발 - 바위들 - 도착 사이의 간격의 최솟값을 구함
# 최솟값 중 최대를 return

# 풀이
# 범위를 보아하니 이분탐색
# rocks는 정렬이 필요한 듯하다.
# 이분탐색은 1. 피봇의 범위, 2. 판단의 기준을 정해야 한다.
# 판단의 기준은 간격의 최솟값
# 피봇의 범위는? 어렵다. n개라서 피봇이 여러 개인 느낌이다.

# 풀이2 참고
# rocks에서 정확히 rock를 집어낼 생각을 버리자
# 거리의 최솟값을 피봇의 범위로 둔다.
# 제거한 바위의 개수를 판단 기준으로 둔다.
# rocks를 탐색하면서, 이전 바위와 거리를 구하고, 해당 거리가 피봇보다 작다면 바위를 제거한다.
# 총 제거한 바위의 개수가, n보다 크다면 너무 많이 제거한 것이다. right = mid - 1
# n과 작거나 같으면, 너무 적게 제거했거나 적절한 것이다. left = mid + 1

def solution(distance, rocks, n):
    answer = 0
    
    left = 0
    right = distance
    
    rocks.sort()
    rocks.append(distance)
    
    while left <= right:
        mid = (left + right) // 2
        
        prev_rock = 0 # 이전 바위의 좌표
        delete = 0 # 삭제한 바위 개수
        
        for rock in rocks:
            dist = rock - prev_rock
            
            if dist < mid: # 현재와 직전 바위 사이 간격이 피봇보다 짧다면, 없어도 되는 것이다.
                delete += 1
                
                if delete > n:
                    break
            else:
                prev_rock = rock
            

        
        if delete > n: # 너무 많이 삭제했다
            right = mid - 1
        else:
            answer = mid
            left = mid + 1
    
    return answer













