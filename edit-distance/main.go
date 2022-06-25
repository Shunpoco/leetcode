package 

func minDistance(word1 string, word2 string) int {
    n := len(word1)
    m := len(word2)
    dp := make([][]int, n+1)
    for r := 0; r < n+1; r++ {
        dp[r] = make([]int, m+1)
        for c := 0; c < m+1; c++ {
            if r == 0 {
                dp[r][c] = c
            } else if c == 0 {
                dp[r][c] = r
            } else {
                v := 1
                if word1[r-1] == word2[c-1] {
                    v = 0
                }
                dp[r][c] = min(
                    dp[r-1][c]+1,
                    dp[r][c-1]+1,
                    dp[r-1][c-1]+v,
                )
            }
        }
    }
    
    // fmt.Println(dp)
    
    
    return dp[n][m]
}

func min(a, b, c int) int {
    result := a
    if result > b {
        result = b
    }
    if result > c {
        result = c
    }
    
    return result
}
