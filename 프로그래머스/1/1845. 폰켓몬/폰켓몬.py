# 문제 분석
# N마리 포켓몬 중에서 N/2마리를 선택한다.
# 이때 선택한 포켓몬의 가짓수가 최대가 되도록 하라.

# 접근
# N마리 포켓몬의 종류가 모두 다른 경우, 최대값은 N/2이다.
# N마리 포켓몬의 종류가 모두 같은 경우, 최대값은 1이다.
# 배열의 길이를 n, 원소의 가짓수를 k라고 하자
    # n/2과 k 중에 작은 값을 return 하면 되겠다.


def solution(nums):
    n = len(nums)
    k = len(set(nums))
    return min(n/2, k)