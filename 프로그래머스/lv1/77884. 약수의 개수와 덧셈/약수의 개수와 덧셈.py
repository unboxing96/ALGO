def solution(left, right):
    # 제곱수 
    result = 0

    # left부터 right까지 탐색
    for num in range(left, right + 1):
        isBool = True
        
        # 1일 때 예외 처리
        if num == 1:
            result -= num
            continue
        
        # num을 1부터 num까지 탐색하며 제곱수 검증, num은 range에서 제외
        for i in range(1, num):
            if i ** 2 == num:
                # 제곱수 있으면 result에서 빼줌
                result -= num
                isBool = False
        # 탐색 후 제곱수 없으면, result에 더해줌
        if isBool:
            result += num

    return result