package main

func maxProfit(prices []int) int {
	n := len(prices)

	hold := make([]int, n)
	free := make([]int, n)

	hold[0] = -prices[0]

	for i := 1; i < n; i++ {
		hold[i] = max([]int{
			hold[i-1],
			free[i-1] - prices[i],
		})
		free[i] = max([]int{
			free[i-1],
			hold[i-1] + prices[i],
		})
	}

	return free[n-1]
}

func max(nums []int) int {
	if nums[0] > nums[1] {
		return nums[0]
	}
	return nums[1]
}
