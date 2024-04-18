import sys
sys.stdin = open("9095.txt", "r")

# 이해
# 정수 n을 1, 2, 3의 합으로 나타내는 방법의 수
# 순서를 구분한다 !!!

# 분석
# dp[1] = 1 / 1
# dp[2] = 2 / 11, 2
# dp[3] = 4 / 111, 12, 21, 3
# dp[4] = 7 / 1111, 112, 121, 211, 22, 13, 31, (4)
# dp[5] = 13 / 11111, 111:2*4, 1:22*3, 11:3*3 23, 32, (14, 41, 5)
# dp[6] = 21?? / 111111, 1:2*5, 11:2*6, 222, 111:3*4, 123*6, 33
# dp[i] = dp[i - 1] + i - 1



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