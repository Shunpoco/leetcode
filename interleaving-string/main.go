package main

func isInterleave(s1 string, s2 string, s3 string) bool {
	n1, n2, n3 := len(s1), len(s2), len(s3)

	if n1+n2 != n3 {
		return false
	}

	dp := make([]bool, n2+1)
	for i := 0; i < n1+1; i++ {
		for j := 0; j < n2+1; j++ {
			if i == 0 && j == 0 {
				dp[j] = true
			} else if i == 0 {
				dp[j] = dp[j-1] && s2[j-1] == s3[i+j-1]
			} else if j == 0 {
				dp[j] = dp[j] && s1[i-1] == s3[i+j-1]
			} else {
				dp[j] = (dp[j-1] && s2[j-1] == s3[i+j-1]) || (dp[j] && s1[i-1] == s3[i+j-1])
			}
		}
	}

	return dp[n2]
}
