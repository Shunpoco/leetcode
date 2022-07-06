package main

func fib(n int) int {
	dp := make([]int, n+1)
	solve(n, &dp)

	return dp[n]
}

func solve(n int, dp *[]int) {
	if n == 0 || (*dp)[n] != 0 {
		return
	}

	var result int
	if n == 1 {
		result = 1
	} else {
		solve(n-1, dp)
		solve(n-2, dp)
		result = (*dp)[n-1] + (*dp)[n-2]
	}

	(*dp)[n] = result
}
