# 이해
# 최대 탑승 가능 무게 limit
# 구명보트를 최대한 적게 사용해서, people을 전부 옮기는 횟수를 return

# 풀이
# heap을 사용해서, 항상 최솟값을 꺼낸다면?
# 반례: 80, [10, 20, 60, 70]
    # 최솟값만 꺼내는 경우: [10, 20], [60], [70] -> 3번
    # 최적: [10, 70], [20, 60] -> 2번
# 완전 탐색 O(N ** 2). N = 50,000이므로 25억이라서 시간 초과 발생할 듯?
# 항상 가장 작은 값과 가장 큰 값을 제거하자.
# people 배열을 오름차순으로 정렬한다. deque으로 만든다.
# while len(people) >= 2
    # people[0] + people[-1]의 값이 limit 보다 작으면 answer += 1 하고, 둘다 제거한다.
    # limit 보다 크면, 큰 값(people[0])만 제거한다. answer += 1
# 마지막에 값이 남아있으면 제거한다. answer += 1

from collections import deque

def solution(people, limit):
    answer = 0
    sorted_people = deque(sorted(people))
    
    while len(sorted_people) >= 2:
        if sorted_people[0] + sorted_people[-1] <= limit:
            sorted_people.popleft()
            sorted_people.pop()
            answer += 1
        else:
            sorted_people.pop()
            answer += 1
    
    if sorted_people:
        answer += 1
    
    return answer








