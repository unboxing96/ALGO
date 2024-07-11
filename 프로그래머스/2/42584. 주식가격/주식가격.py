# 문제 분석
# 탑 보기, 올영 코테와 비슷한 문제
# 차이점은 건물 뒤편까지 판단해야 한다는 것

# 접근
# answer를 초기화 한다. 배열의 각 요소가 얻을 수 있는 최대값으로 한다.
# stack을 초기화 한다.
# prices 배열을 탐색한다. (1, n)
    # while stack and prices[stack[-1]] > prices[i]:
        # j = stack.pop()
        # answer[i] = i - j
    # stack.append(i)

def solution(prices):
    answer = [i for i in range(len(prices) - 1, -1, -1)]
    stack = [0]
    
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)

    return answer