# 문제 분석
# progresses는 현재까지 진도를 담고 있다. 인덱스가 곧 배포 순서이다.
# speeds는 개발 속도이다.
# 매일 speed만큼 진도를 나간다.(progresses 배열의 원소에 더한다)
# progress가 100이 되면 배포 준비를 마친다.
# 가장 앞에 있는 progress가 배포 준비를 마치면 즉시 배포된다.
    # 이때, 앞에서부터 순서대로 배포 준비를 마친 것들이 모두 배포된다.
    
# 접근
# progresses와 speeds를 동시에 탐색하며, 배포까지 남은 일수를 구한다. (leftovers)
# leftovers를 뒤집는다. 스택 연산으로 게산하기 편하게.
# top 요소를 제거하면서, 해당 값 이하의 요소도 모두 제거한다.
    # 제거하는 수만큼 count해서 answer에 추가한다.
# answer를 return 한다.

def solution(progresses, speeds):
    answer = []
    leftovers = []
    
    for i in range(len(progresses)):
        quotient = (100 - progresses[i]) // speeds[i]
        remainder = (100 - progresses[i]) % speeds[i]
        if remainder:
            quotient += 1
        leftovers.append(quotient)
    
    leftovers.reverse()
    
    while leftovers:
        top = leftovers.pop()
        cnt = 1
        while leftovers and leftovers[-1] <= top:
            leftovers.pop()
            cnt += 1
        answer.append(cnt)
        
    return answer