let n = Int(readLine()!)!

func solution(n: Int) -> Int {
    
    if n == 3 { return 1}
    if n == 4 { return -1 }
    
    var dp = Array(repeating: 5001, count: n + 1)
    dp[3] = 1
    dp[5] = 1
    
    for i in 6..<n+1 {
        dp[i] = min(dp[i - 3], dp[i - 5]) + 1
    }
    
    return dp[n] < 5001 ? dp[n] : -1
}

print(solution(n: n))