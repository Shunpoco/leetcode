package main

func maxProfit(prices []int, fee int) int {
	n := len(prices)

	hold := make([]int, n)
	free := make([]int, n)

	hold[0] = -prices[0]

	for i := 1; i < n; i++ {
		hold[i] = max(hold[i-1], free[i-1]-prices[i])
		free[i] = max(free[i-1], hold[i-1]+prices[i]-fee)
	}

	return free[n-1]
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
