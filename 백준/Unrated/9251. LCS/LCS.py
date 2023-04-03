word1 = input()
word2 = input()

graph = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]


for i in range(1, len(word1) + 1):
    for j in range(1, len(word2) + 1):
        if word1[i - 1] == word2[j - 1]:
            graph[i][j] = graph[i - 1][j - 1] + 1
        else:
            graph[i][j] = max(graph[i - 1][j], graph[i][j - 1])

print(graph[-1][-1])