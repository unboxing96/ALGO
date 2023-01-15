# 퀸은 한 행에 하나씩만 가능
# 같은 열 체크 + 왼쪽 아래 대각선 + 오른쪽 아래 대각선 체크
# 끝까지 재귀 성공하면 ans += 1


n = int(input())
row = [0] * n


def is_promising(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x - i):
            return False
    return True


def n_queens(x):
    global ans
    if x == n:
        ans += 1
        return True
    else:
        for i in range(n):
            row[x] = i
            if is_promising(x):
                n_queens(x + 1)


ans = 0
n_queens(0)
print(ans)
