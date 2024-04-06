# 이해
# numbers에 있는 모든 원소는 부호를 가질 수 있다.
# 부호를 포함한 모든 원소의 합이 target이 되는 경우의 가짓수를 구하는 문제이다.

# 풀이
# 모든 경우의 수를 따지는 것이 좋겠다.
# 무작정 완전 탐색은 O(2^20)이므로 불가하다.
# DFS로 풀이하자.
# 재귀적으로 +인 경우와, -인 경우를 동시에 호출하자.
# 깊이(배열의 index)를 추적하여 numbers의 길이와 같아지는 경우, target을 달성했는지를 검증하고 result += 1 하자.
# 모든 탐색이 종료되고 result를 return 하자.

def solution(numbers, target):
    return dfs(0, 0, numbers, target)

def dfs(depth, tot_sum, numbers, target):    
    if depth == len(numbers):
        if tot_sum == target:
            return 1
        return 0

    return dfs(depth + 1, tot_sum + numbers[depth], numbers, target) + dfs(depth + 1, tot_sum - numbers[depth], numbers, target)