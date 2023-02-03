n, m, v = map(int, input().split())

graph = [[0] * (n + 1) for i in range(n + 1)]
visited = [0] * (n + 1)

# 인접 행렬 생성 (edge만큼 반복)
for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(v):
    # 방문한 노드 += 1
    visited[v] = 1

    print(v, end=" ")

    # 행렬과 방문 노드 순회
    for i in range(1, n + 1):
        # 인접 행렬이지만, 아직 방문하지 않은 노드일 때
        if graph[v][i] == 1 and visited[i] == 0:
            dfs(i)


def bfs(v):
    # 방문해야 할 곳을 순서대로 넣을 큐
    q = [v]

    # 방문한 곳은 visited를 다시 0으로
    visited[v] = 0

    while q:
        # 큐에서 처음 올린 노드 꺼내줌
        v = q.pop(0)
        print(v, end=" ")

        # 행렬과 방문 노드 순회
        for i in range(1, n + 1):
            if graph[v][i] == 1 and visited[i] == 1:
                q.append(i)
                visited[i] = 0


dfs(v)
print("")
bfs(v)