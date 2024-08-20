# 문제 분석
# numbers에 숫자로 구성된 문자열이 주어진다.
# numbers의 각 문자를 조합해서 정수를 만들고, 개중에서 소수의 개수를 구하라

# 접근
# 일종의 순열이다. 순열의 시간 복잡도는 O(N!). 입력값이 7이므로, 7! == 5,040.
# 숫자 조합을 찾아내면, 최고값을 기준으로 에라토스테네스의 체를 만든다.
# 체 배열을 탐색하며, 소수의 개수를 세어 return 한다.

# 순열
# DFS와 백트래킹
# 배열의 길이와 같은 visited 배열을 생성한다.
# 순열을 담을 임시 배열을 만든다. perm = []
# permutation 함수는 depth 파라미터로 탈출 조건을 만든다.
    # 모든 원소를 다 썼을 경우 탈출한다.
# 방문하지 않은 원소인 경우, 방문 처리하고, perm에 추가하고, 재귀 탐색하고, perm에서 pop() 하고, 방문 처리를 취소한다.
# targetDepth 별로 순열을 구한다.

# 에라토스 테네스의 체
# 입력된 정수 n까지 소수만 남기고 탈탈 털어내는 체
# n ** 0.5 까지만 탐색하면, n의 소수 여부를 판별할 수 있다는 것을 유념하자.
# 범위 내 전체 정수 리스트primeArr를 set 과 range로 생성한다.
# 전체 정수 범위를 탐색한다.
# 현재 탐색 중인 정수가, primeArr에 없다면, range로 정수의 배수 배열을 만들어서 primeArr에서 뺀다. (집합 연산으로)
# 남은 것이 소수 리스트이다.

def solution(numbers):
    answer = 0
    candidates = set()
    visited = [False] * len(numbers)
    
    for i in range(1, len(numbers) + 1):
        permutation(numbers, visited, candidates, [], i, 0)
    
    maxNum = max(candidates)
    primeSet = eratos(maxNum)
    
    return len(candidates & primeSet)

def permutation(numbers, visited, candidates, perm, targetDepth, currentDepth):
    if currentDepth == targetDepth:
        candidates.add(int("".join(perm)))
    
    for i in range(len(numbers)):
        if not visited[i]:
            visited[i] = True
            perm.append(numbers[i])
            permutation(numbers, visited, candidates, perm, targetDepth, currentDepth + 1)
            perm.pop()
            visited[i] = False
            
            
            
def eratos(target):
    primeSet = set(range(2, target + 1))
    
    for i in range(2, int(target ** 0.5) + 1):
        if i in primeSet:
            primeSet -= set(range(2 * i, target + 1, i))
    
    return primeSet