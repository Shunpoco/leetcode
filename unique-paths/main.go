package main

func uniquePaths(m int, n int) int {

	dp := make([]int, n+1)

	for i := 1; i < m+1; i++ {
		for j := 0; j < n+1; j++ {
			if j == 0 {
				dp[j] = 0
			} else if i == 1 && j == 1 {
				dp[j] = 1
			} else {
				dp[j] = dp[j] + dp[j-1]
			}
		}
	}

	return dp[n]
}
