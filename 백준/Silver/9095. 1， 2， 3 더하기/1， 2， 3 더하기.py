n = int(input())

for tc in range(n):
    target = int(input())
    dp = [0] * (target + 1)

    for i in range(1, target + 1):

        if i == 1:
            dp[1] = 1
        elif i == 2:
            dp[2] = 2
        elif i == 3:
            dp[3] = 4
        else:
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    
    print(dp[target])