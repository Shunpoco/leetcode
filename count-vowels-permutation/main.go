package main

func countVowelPermutation(n int) int {
    MOD := 1000000007
    
    dp := make([][]int, n+1)
    
    for i := 0; i < n+1; i++ {
        dp[i] = make([]int, 5)
        for j := 0; j < 5; j++ {
            if i == 0 {
                dp[i][j] = 0
            } else if i == 1 {
                dp[i][j] = 1
            } else if j == 0 {
                dp[i][j] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
            } else if j == 1 {
                dp[i][j] = dp[i-1][0] + dp[i-1][2]
            } else if j == 2 {
                dp[i][j] = dp[i-1][1] + dp[i-1][3]
            } else if j == 3 {
                dp[i][j] = dp[i-1][2]
            } else {
                dp[i][j] = dp[i-1][2] + dp[i-1][3]
            }
            dp[i][j] %= MOD
        }
    }
    
    var result int
    for j := 0; j < 5; j++ {
        result += dp[n][j]
        result %= MOD
    }
    
    return result
}
