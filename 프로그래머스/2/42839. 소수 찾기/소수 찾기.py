# 이해
# 생성 가능한 소수의 개수를 return
# 1. 주어진 숫자 카드로 만들 수 있는 조합을 모두 생성. P(7, 1) + P(7, 2), ... P(7, 7) ~= 14,000
# 2. 숫자 카드의 최대 길이인 9,999,999 까지의 소수를 에라토스테네스의 체로 구함
# 3. 생성된 조합을 탐색하며, 2번에서 생성한 소수 배열에 있으면 answer += 1

# 풀이
# 수열 생성 함수 def permute(arr, n):
# 방문 처리를 위한 used 배열 생성 [False] * len(numbers)
# 탈출 조건: 
    # if len(arr) == n:
        # num = int("".join(arr))
        # permutations.add(num)
    # else: # 순열 생성 연산: 백트래킹
        # for i in range(len(numbers)):
            # if not used[i]:
                # used[i] = True
                # permute(arr + [numbers[i]], n)
                # user[i] = False


def solution(numbers):
    
    def permute(arr, n):
        if len(arr) == n:
            num = int("".join(arr))
            permutations.add(num)
        else:
            for i in range(len(numbers)):
                if not used[i]:
                    used[i] = True
                    permute(arr + [numbers[i]], n)
                    used[i] = False
                    
    def eratos(n):
        eratos_arr = [True] * (n + 1)
        eratos_arr[0] = eratos_arr[1] = False
        
        for i in range(int(n ** 0.5) + 1):
            if eratos_arr[i]:
                for j in range(i * i, n + 1, i):
                    eratos_arr[j] = False
        
        return eratos_arr

    answer = 0
    used = [False] * len(numbers)
    permutations = set()
    
    for i in range(1, len(numbers) + 1):
        permute([], i)
    
    prime_arr = eratos(max(permutations))
    
    return sum(1 for num in permutations if prime_arr[num])















