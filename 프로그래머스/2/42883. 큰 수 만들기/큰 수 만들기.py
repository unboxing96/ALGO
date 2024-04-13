# 이해
# 남은 숫자가 최대가 되도록, number 중에서 k개를 제거한다.
# 남은 숫자를 return 한다.
# 남은 숫자를 정렬하면 안 된다는 것이 핵심이다.
# n은 1,000,000 이므로 O(N ** 2)은 곤란한다.
# 최소 힙을 사용하면 쉽겠다. 이렇게 먼저 풀고, 이후에 그리디 하게 풀어보자.

# 풀이
# 등장하는 수를 Counter로 카운트 한다. O(N)
# Counter를 탐색한다. 가장 낮은 값부터 k개까지 모아둔다. 이것만큼만 number에서 삭제할 것이다.
# number를 탐색하면서, 모아둔 값과 일치하는 값을 만나면 pass 하고 모아둔 값에서 삭제한다. 일치하지 않는 값은 정답 문자열에 추가한다.

def solution(number, k):
    
    stack = []
    for num in number:
        while k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    return "".join(stack[:len(number) - k])








