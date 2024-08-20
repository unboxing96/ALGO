# 문제 분석
# 입력으로 주어진 숫자를, 문자열로 취급하여서 이어붙여 만든 숫자 중에서, 최대값 return

# 접근
# 모든 경우의 수를 구하는 것(순열)은 O(N!)이다. 이건 절대 안 된다.
# 정렬을 하면 [2, 6 ,10]과 같은 형태로 정렬이 되어서, 의도대로 되지 않는다.
# 입력값을 문자열로 취급하여서, 정렬을 하면 어떨까? -> ["10", "2", "6"] 형태로 정렬이 된다. 반례는 없을까?
    # 아래 예제의 경우 30이 3보다 높은 우선 순위를 갖는다. 어떻게 해결할까?
    # 각 원소를 반복하여 3자리 숫자로 확장한 다음에 비교를 하면 되겠다.
    # 333, 303 343, 555, 999 -> 999, 555, 343, 333, 303으로 될 것이다.
    # 비교 후에는 다시 원래 원소를 입력해야 한다.

# 그냥 정렬할 때 람다식으로 1. 문자열로 만들고, 2. 3자리가 되도록 반복하면 되지 않을까?
    # 함수 만들자 그냥 ...
    # repeatString(int) -> string:
        # stringNum = str(int)
        # slicedNum = (stringNum * 3)[:3]
        # return slicedNum # 303
# 그 다음에 정렬된 것을 문자열로 붙여서 return 하면 끝.

def repeatString(num):
    stringNum = str(num)
    slicedNum = (stringNum * 3)

    return slicedNum

def solution(numbers):
    answer = ""
    sortedNum = sorted(numbers, key = lambda x : repeatString(x), reverse = True)
    
    for num in sortedNum:
        answer += str(num)

    return str(int(answer))