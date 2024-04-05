# 접근
# 1. 주어진 숫자 카드로 만들 수 있는 조합을 모두 생성. P(7, 1) + P(7, 2), ... P(7, 7) ~= 14,000
# 2. 숫자 카드의 최대 길이인 9,999,999 까지의 소수를 에라토스테네스의 체로 구함
# 3. 생성된 조합을 탐색하며, 2번에서 생성한 소수 배열에 있으면 answer += 1

def solution(numbers):
    def permute(arr, n):
        # 현재 길이가 n이면, 결과에 추가
        if len(arr) == n:
            num = int("".join(arr))
            perms.add(num)
        else:
            for i in range(len(numbers)):
                if not used[i]:
                    used[i] = True
                    permute(arr + [numbers[i]], n)
                    used[i] = False

    def eratos(n):
        sieve = [True] * (n + 1)
        sieve[0] = sieve[1] = False
        for i in range(2, int(n**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, n+1, i):
                    sieve[j] = False
        return sieve

    perms = set()
    used = [False] * len(numbers)
    # 모든 길이의 조합 생성
    for i in range(1, len(numbers) + 1):
        permute([], i)

    max_num = max(perms)
    sieve = eratos(max_num)
    answer = sum(1 for num in perms if sieve[num])

    return answer