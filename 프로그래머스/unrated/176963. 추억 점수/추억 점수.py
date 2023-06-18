from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    score = defaultdict(int)

    for i in range(len(name)):
        score[name[i]] = yearning[i]

    for pho in photo:
        tmp = 0
        for i in range(len(pho)):
            tmp += score[pho[i]]
        
        answer.append(tmp)

    return answer