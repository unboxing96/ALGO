def solution(N, stages):
    size = len(stages)
    dic = {}
    for i in range(1, N + 1):
        num = stages.count(i)
        if size == 0:
            dic[i] = 0
        else:
            dic[i] = num / size
        size -= num
    return sorted(dic, key=lambda x: dic[x], reverse=True)
