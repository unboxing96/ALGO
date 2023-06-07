
n = int(input())
ans = []

def check():

    if len(ans) == n:
        print(*ans, sep=" ")
        return

    for i in range(1, n + 1):
        if i not in ans:
            ans.append(i)
            check()
            ans.pop()

check()