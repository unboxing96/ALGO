import heapq

def dijkstra(gates, graph, n, summits_set):
    INF = int(1e9)
    # 가장 먼저 해당 노드에 도달한 경우. 출입구 ~ 해당 노드까지 intensity
    intensity = [INF] * (n + 1)
    h = []
    
    # 출입구를 시작점으로 하는 초기 설정
    for gate in gates:
        heapq.heappush(h, (0, gate))  # (intensity, node)
        intensity[gate] = 0
    
    while h:
        now_intensity, now = heapq.heappop(h)

        # 현재 비용 > 기록되어 있는 비용이라면 진행X
        if now_intensity > intensity[now]:
            continue
        
        # 산봉우리 노드라면 탐색 중단
        if now in summits_set:
            continue
        
        # 현재 노드와 연결된 노드들 탐색
        for next_intensity, next in graph[now]:
            max_intensity_in_current_path = max(now_intensity, next_intensity) # max_intensity_in_current_path: 현재 탐색 중인 경로의 intensity 중 최댓값
            if intensity[next] > max_intensity_in_current_path: # intensity[node]: 다른 경로를 통해 next에 도달한 경우의 intensity
                intensity[next] = max_intensity_in_current_path # 다른 경로보다 현재 경로가 효율적인 경우 갱신
                heapq.heappush(h, (max_intensity_in_current_path, next))
    
    return intensity

def solution(n, paths, gates, summits):
    # 인접 리스트 형태로 그래프 만들기
    graph = [[] for _ in range(n + 1)]
    for path in paths:
        a, b, c = path
        graph[a].append((c, b))
        graph[b].append((c, a))
    
    summits_set = set(summits)  # in 연산 시간 감소를 위해
    
    # 출입구에서 시작하는 다익스트라 알고리즘 실행
    intensity = dijkstra(gates, graph, n, summits_set)
    
    # 산봉우리 중에서 intensity가 최소인 산봉우리 찾기
    answer_summit = -1
    answer_intensity = int(1e9)
    
    for summit in sorted(summits):
        if intensity[summit] < answer_intensity:
            answer_intensity = intensity[summit]
            answer_summit = summit
    
    return [answer_summit, answer_intensity]