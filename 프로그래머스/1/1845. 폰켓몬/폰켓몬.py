# 이해
# N마리 중에서 N/2마리를 선택.
# 이때 가장 많은 종류를 선택하고, 그때의 가짓수를 return
# nums의 길이는 10,000이므로 O(n^2)까지는 괜찮겠다. 프로그래머스는 10억에서 시간 초과가 발생하므로.

# 풀이
# nums+1(0부터 200,000) 크기의 visited 배열을 만든다.
# nums를 탐색하며, 방문하지 않은 포켓몬일 경우 result, cnt에 += 1 하고, 방문 처리한다.
# 매 탐색마다 cnt가 len(nums) // 2 이하인지 확인한다. 초과하면 result를 return 한다.

def solution(nums):
    cnt = 0
    size = len(nums)
    visited = [False] * (size + 1)
    variety = len(set(nums))
    
    if variety <= size // 2:
        return variety
    
    for i, num in enumerate(nums):
        if not visited[i]:
            visited[i] = True
            
            if cnt + 1 <= size // 2:
                cnt += 1
            else:
                break
    
    return cnt