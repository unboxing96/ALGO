def solution(n, s, a, b, fares):

    # 거리 초기화
    INF = int(1e9)
    dist = [[INF] * (n + 1) for _ in range(n + 1)]
    answer = INF

    # 자기 자신 0으로 초기화
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                dist[i][j] = 0

    # 가중치 초기화
    for i, j, cost in fares:
        dist[i][j] = dist[j][i] = cost

    # 최소 거리로 초기화
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    for i in range(1, n + 1):
        cost = dist[s][i] + dist[i][a] + dist[i][b]
        answer = min(answer, cost)

    return answer
