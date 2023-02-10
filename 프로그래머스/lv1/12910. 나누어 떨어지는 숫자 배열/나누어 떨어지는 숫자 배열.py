def solution(arr, divisor):
    answer = []
    
    arr.sort()
    for a in arr:
        if a % divisor == 0:
            answer.append(a)
    
    if not answer:
        return [-1]
    else:
        return answer