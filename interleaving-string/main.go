package main

func isInterleave(s1 string, s2 string, s3 string) bool {
    n1 := len(s1)
    n2 := len(s2)
    n3 := len(s3)
    
    if n1+n2 != n3 {
        return false
    }
    
    dp := make([][]bool, n1+1)
    for i := 0; i < n1+1; i++ {
        dp[i] = make([]bool, n2+1)
        for j := 0; j < n2+1; j++ {
            if i == 0 && j == 0 {
                dp[i][j] = true
            } else if i == 0 {
                dp[i][j] = dp[i][j-1] && s2[j-1] == s3[i+j-1]
            } else if j == 0 {
                dp[i][j] = dp[i-1][j] && s1[i-1] == s3[i+j-1]
            } else {
                dp[i][j] = (dp[i][j-1] && s2[j-1] == s3[i+j-1]) || (dp[i-1][j] && s1[i-1] == s3[i+j-1])
            }
        }
    }
    
    return dp[n1][n2]    
}
