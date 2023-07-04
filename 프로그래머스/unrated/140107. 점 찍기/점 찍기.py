import math

def solution(k, d):
    answer = 0

    for a in range(d//k + 1):
        b_max = math.floor(math.sqrt(d**2 - (a*k)**2) // k)
        answer += b_max + 1

    return answer
