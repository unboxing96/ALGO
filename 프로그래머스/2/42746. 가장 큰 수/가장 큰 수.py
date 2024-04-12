# 이해
# 문자열로 된 숫자를 조합해서, 생성 가능한 숫자 중 가장 큰 수 return

# 풀이
# numbers를 문자열의 배열로 변환
# 내림차순 정렬
# 배열 내의 원소를 하나로 합침

# 문제
# 문제의 조건에 따르면 우선순위가 다음과 같아야 함. 3 > 30
# 그러나 일반적인 정렬은 다음과 같이 정렬됨. 30 > 3
# 문제의 의도대로 정렬이 되려면, 3은 33으로 취급해야 함.

def solution(numbers):
    str_numbers = list(map(str, numbers))
    
    # 각 숫자를 3자리까지 늘려줍니다.
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    
    # 배열 내의 원소를 하나로 합칩니다.
    answer = ''.join(str_numbers)
    
    # 모든 숫자가 0으로 이루어진 경우에는 '0000...' 이런 식으로 반환될 수 있으므로
    # 이 경우 0 하나만 반환해줍니다.
    return str(int(answer))