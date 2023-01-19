
def solution(rows, columns, queries):

    res = []

    # generate graph
    check = [[False] * (columns + 1) for _ in range(rows + 1)]

    # generate graph
    graph = [[0] * (columns + 1) for _ in range(rows + 1)]
    k = 1
    for i in range(1, rows + 1):
        for j in range(1, columns + 1):
            graph[i][j] = k
            k += 1

    for q in queries:

        # check new numbers
        visited = [[0] * (columns + 1) for _ in range(rows + 1)]

        x1, y1, x2, y2 = q[0], q[1], q[2], q[3]

        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                # 첫 행
                if i == x1:
                    if j == y2:
                        if not visited[i + 1][j]:
                            visited[i + 1][j] = graph[i][j]
                            check[i + 1][j] = True
                    else:
                        if not visited[i][j + 1]:
                            visited[i][j + 1] = graph[i][j]
                            check[i][j + 1] = True
                # 끝 열
                if j == y2:
                    if i == x2:
                        if not visited[i][j - 1]:
                            visited[i][j - 1] = graph[i][j]
                            check[i][j - 1] = True
                    else:
                        if not visited[i + 1][j]:
                            visited[i + 1][j] = graph[i][j]
                            check[i + 1][j] = True

                # 끝 행
                if i == x2:
                    if j == y1:
                        if not visited[i - 1][j]:
                            visited[i - 1][j] = graph[i][j]
                            check[i - 1][j] = True
                    else:
                        if not visited[i][j - 1]:
                            visited[i][j - 1] = graph[i][j]
                            check[i][j - 1] = True

                # 첫 열
                if j == y1:
                    if i == x1:
                        if not visited[i][j + 1]:
                            visited[i][j + 1] = graph[i][j]
                            check[i][j + 1] = True
                    else:
                        if not visited[i - 1][j]:
                            visited[i - 1][j] = graph[i][j]
                            check[i - 1][j] = True

        for i in range(1, rows + 1):
            for j in range(1, columns + 1):
                if visited[i][j]:
                    graph[i][j] = visited[i][j]

        bottom = 1e9
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if visited[i][j] and visited[i][j] < bottom:
                    bottom = visited[i][j]

        res.append(bottom)

    return res
