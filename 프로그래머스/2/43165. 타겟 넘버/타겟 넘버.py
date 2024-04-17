# 이해
# numbers에 주어진 원소를 더하거나 빼서 target을 완성시키는 방법의 수

# 풀이
# DFS로 모든 가능성을 탐색한다.
# 2 ** 20 ~= 1,000,000 이므로 문제 없다.
# 2 ** 30 ~= 1,000,000,000이므로 2 ** 29까지는 문제 없을 것이다. O(N) 기준.

# numbers를 탐색한다.
# 1. number를 더하기 한 것을 재귀적으로 호출한다.
# 2. number를 빼기 한 것을 재귀적으로 호출한다.
# cnt == target이 되면 answer += 1
# answer를 return

cnt = 0

def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return cnt

def dfs(numbers, target, current, idx):
    global cnt
    if idx == len(numbers):
        if current == target:
            cnt += 1
        return
    
    dfs(numbers, target, current + numbers[idx], idx + 1)
    dfs(numbers, target, current - numbers[idx], idx + 1)
    
    
    
    
    
    
    
    
    
    
    