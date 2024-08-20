def solve(i, total):
    global n, target, res

    if i == n:
        if total >= target:
            res = min(res, total - target)
        return

    solve(i + 1, total + heights[i])
    solve(i + 1, total)


T = int(input())
for tc in range(T):
    n, target = map(int, input().split())
    heights = list(map(int, input().split()))
    res = 1e9
    solve(0, 0)
    print(f'#{tc + 1} {res}')