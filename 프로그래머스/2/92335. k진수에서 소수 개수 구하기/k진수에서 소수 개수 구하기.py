# 문제 분석
# n을 k진수로 바꾼 뒤, 문자열로 변환
# 문자열을 0으로 분리
# 분리된 문자열을 10진법으로 보았을 때 소수인 것의 개수를 return

# 소수 판별 함수는 n ** 0.5의 시간복잡도를 갖는다.
# n의 범위가 1,000,000이므로 가능

# k진수 만드는 함수 구현
# 정수형 n을 k로 계속 나누고, after_num_list 배열에 추가한 뒤, 마지막에 뒤집는다.

def decimal_to_k_num(n, k):
    after_num_list = []
    while n > 0:
        after_num_list.append(n % k)
        n //= k
    return "".join(map(str, after_num_list[::-1]))

def is_prime(num):
    if len(num) < 1:
        return False
    
    num = int(num)
    if num < 2:
        return False
    
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = -1
    
    k_num = decimal_to_k_num(n, k)
    splited_k_num = k_num.split("0")
    
    cnt = 0
    for num in splited_k_num:
        if is_prime(num):
            cnt += 1
    
    return cnt