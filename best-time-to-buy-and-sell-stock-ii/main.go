package main

func maxProfit(prices []int) int {
	n := len(prices)

	dp := make([]int, n+1)

	for i := 1; i <= n; i++ {
		for j := i; j <= n; j++ {
			dp[j] = max([]int{dp[i-1] + (prices[j-1] - prices[i-1]), dp[j-1], dp[j]})
		}
	}

	return dp[n]
}

func max(nums []int) int {
	var result int

	for _, num := range nums {
		if result < num {
			result = num
		}
	}

	return result
}
