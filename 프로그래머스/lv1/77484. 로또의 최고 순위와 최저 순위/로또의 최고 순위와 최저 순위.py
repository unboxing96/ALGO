def solution(lottos, win_nums):
    
    correct = []

    for i in lottos:
        if i in win_nums:
            correct.append(i)

    good = len(correct) + lottos.count(0)
    bad = len(correct)

    answer = []

    for score in [good, bad]:
        if score < 2:
            answer.append(6)
        else:
            answer.append(7 - score)
            
    return answer
