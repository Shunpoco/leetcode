package main

func minimumDeleteSum(s1 string, s2 string) int {
    n := len(s1)
    m := len(s2)

    dp := make([][]int, n+1)
    for row := 0; row < n+1; row++ {
        dp[row] = make([]int, m+1)
        for col := 0; col < m+1; col++ {
            if row == 0 && col == 0{
                dp[row][col] = 0
            } else if row == 0 {
                dp[row][col] = dp[row][col-1] + int(s2[col-1])
            } else if col == 0 {
                dp[row][col] = dp[row-1][col] + int(s1[row-1])
            } else {
                v := dp[row-1][col] + int(s1[row-1])
                if v > dp[row][col-1] + int(s2[col-1]) {
                    v = dp[row][col-1] + int(s2[col-1])
                }
                if s1[row-1] == s2[col-1] && v > dp[row-1][col-1] {
                    v = dp[row-1][col-1]
                }

                dp[row][col] = v
            }
        }
    }

    // fmt.Println(dp)
    
    return dp[n][m]
}
