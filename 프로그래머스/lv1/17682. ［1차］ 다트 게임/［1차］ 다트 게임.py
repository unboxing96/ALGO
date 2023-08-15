def solution(dartResult):
    score = []
    i = 0

    while i < len(dartResult):
        # 10 처리
        if dartResult[i] == '1' and dartResult[i + 1] == '0':
            dartResult_to_int = 10
            i += 1
        else:
            dartResult_to_int = int(dartResult[i])

        i += 1

        if dartResult[i] == 'S':
            score.append(dartResult_to_int)
        elif dartResult[i] == 'D':
            score.append(dartResult_to_int**2)
        elif dartResult[i] == 'T':
            score.append(dartResult_to_int**3)

        i += 1
        
        if i < len(dartResult) and dartResult[i] == '*':
            if len(score) >= 2:
                score[-2] *= 2
            score[-1] *= 2
            i += 1
        elif i < len(dartResult) and dartResult[i] == '#':
            score[-1] *= -1
            i += 1
            
    return sum(score)
