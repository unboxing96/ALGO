def solution(cards):
    answer = []
    visited = [False] * (len(cards)+1)

    for node in cards:
        if not visited[node]:
            tmp = []
            while node not in tmp:
                tmp.append(node)
                node = cards[node-1]
                visited[node] = True
            
            answer.append(len(tmp))

    if answer[0] == len(cards):
        return 0
    else:
        answer.sort(reverse=True)

    return answer[0] * answer[1]

cards = [8,6,3,7,2,5,1,4]
print(solution(cards))