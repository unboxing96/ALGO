def solution(n):
    if n == 1:
        answer = 1
        return answer
    nums = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            nums.append(i)
            nums.append(n // i)
    answer = sum(set(nums))
    return answer


print(solution(25))
