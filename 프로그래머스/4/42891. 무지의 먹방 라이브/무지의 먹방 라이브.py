def solution(food_times, k):
    # 음식 시간과 인덱스를 함께 저장하고 음식 시간을 기준으로 정렬
    foods = [(time, idx) for idx, time in enumerate(food_times)]
    foods.sort()
    
    n = len(food_times)
    prev_time = 0  # 이전에 제거한 음식 시간
    for i, (time, idx) in enumerate(foods):
        diff = time - prev_time
        if diff != 0:
            total_eat_time = diff * n  # 현재 레벨에서 모두 먹는데 걸리는 시간
            if total_eat_time <= k:
                k -= total_eat_time
                prev_time = time  # 이전 시간 갱신
            else:
                k %= n  # 남은 음식 중에서 k번째를 찾기 위해 나머지 연산
                remaining_foods = sorted(foods[i:], key=lambda x: x[1])
                return remaining_foods[k][1] + 1
        n -= 1  # 하나의 레벨을 제거했으므로 전체 음식 개수 감소
    
    return -1  # 더 이상 먹을 음식이 없으면 -1 반환

print(solution([3, 1, 2], 5))  # 예시 테스트 케이스