def solve(n, total):
    global N, target, res

    if n == N:
        if total >= target:
            res = min(res, total - target)
        return

    solve(n + 1, total + heights[n])
    solve(n + 1, total)


T = int(input())
for tc in range(T):
    N, target = map(int, input().split())
    heights = list(map(int, input().split()))
    res = 1e9
    solve(0, 0)
    print(f'#{tc + 1} {res}')