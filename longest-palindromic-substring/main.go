package main

// func longestPalindrome(s string) string {
// 	n := len(s)

// 	if n == 0 {
// 		return ""
// 	}

// 	start := 0
// 	end := 0

// 	for i := 0; i < n; i++ {
// 		l1 := window(s, i, i)
// 		l2 := window(s, i, i+1)

// 		l := l1
// 		if l < l2 {
// 			l = l2
// 		}

// 		if l > end-start {
// 			start = i - (l-1)/2
// 			end = i + l/2
// 		}
// 	}

// 	return s[start : end+1]
// }

// func window(s string, left, right int) int {
// 	l := left
// 	r := right

// 	for l >= 0 && r < len(s) && s[l] == s[r] {
// 		l--
// 		r++
// 	}

// 	return r - l - 1
// }

func longestPalindrome(s string) string {
	n := len(s)
	dp := make([][]bool, n)
	start := 0
	end := 0

	for i := 0; i < n; i++ {
		dp[i] = make([]bool, n)
		dp[i][i] = true
		if i < n-1 {
			if s[i] == s[i+1] {
				dp[i][i+1] = true
				start = i
				end = i + 1
			} else {
				dp[i][i+1] = false
			}
		}
	}

	for i := n - 1; i >= 0; i-- {
		for j := i + 2; j < n; j++ {
			if dp[i+1][j-1] && s[i] == s[j] {
				dp[i][j] = true
				if j-i+1 > end-start+1 {
					start = i
					end = j
				}
			} else {
				dp[i][j] = false
			}
		}
	}

	return s[start : end+1]
}
