def solution(n, s, a, b, fares):
    answer = 10 ** 9
    cost = [[answer] * (n+1) for _ in range(n+1)]
    
    def floyd():
        for k in range(n+1):
            for i in range(n+1):
                for j in range(n+1):
                    if i == j:
                        cost[i][j] = 0
                    else:
                        cost[i][j] = min(cost[i][j], cost[i][k] + cost[k][j])
                        
    for i, j, c in fares:
        cost[i][j] = c
        cost[j][i] = c
    floyd()
    
    for i in range(1, n+1):
        answer = min(answer, cost[s][i] + cost[i][a] + cost[i][b])
    return answer