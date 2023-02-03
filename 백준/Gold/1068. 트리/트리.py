def dfs(v):
    tree[v] = -2  # 제거 처리
    for i in range(n):
        if tree[i] == v:  # i 노드의 부모가 == 제거할 노드라면
            dfs(i)  # 제거


# 입력 받기
n = int(input())
tree = list(map(int, input().split()))
erase = int(input())

# 제거할 노드 dfs
dfs(erase)

# dfs 종료 되면, tree 돌면서 리프 노드 cnt
cnt = 0
for i in range(n):
    # 부모 노드(tree[i])가 제거되지 않았고 and 현재 노드(i)가 부모 노드 리스트에 없다면 == 리프 노드
    if tree[i] != -2 and i not in tree:
        cnt += 1

print(cnt)
