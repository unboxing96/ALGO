def solution(n):
    arr = [0, 0] + [1 for _ in range(n - 1)]

    for i in range(2, int(n ** 0.5) + 1):
        if arr[i] == 1: # i가 소수라면
            j = 2
            while i * j <= n:
                arr[i * j] = 0 # 체로 거르기 == 소수 아님
                j += 1

    return sum(arr)