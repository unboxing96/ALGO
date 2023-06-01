n, m = map(int, input().split())
ans = []

def check():

    if len(ans) == m:
        print(*ans, sep=" ")
        return

    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            check()
            ans.pop()

check()