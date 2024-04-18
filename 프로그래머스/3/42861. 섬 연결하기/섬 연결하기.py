# 플로이드 와샬
# 최단 경로 테이블 갱신
# 0번 노드에서 출발해서, 매번 연결 노드 중 최단 거리 노드를 선택한다.

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    rootA = find(parent, a)
    rootB = find(parent, b)
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

def solution(n, costs):
    costs.sort(key=lambda x: x[2])  # 간선을 비용에 따라 오름차순으로 정렬
    parent = [i for i in range(n)]  # 부모 테이블 초기화

    total_cost = 0
    for cost in costs:
        a, b, c = cost
        if find(parent, a) != find(parent, b):  # 사이클이 발생하지 않는 경우
            union(parent, a, b)
            total_cost += c  # 해당 간선을 결과에 추가
    
    return total_cost