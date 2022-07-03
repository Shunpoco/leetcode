package main

type Tuple struct {
	num int
	val int
}

func wiggleMaxLength(nums []int) int {
	n := len(nums)

	dp := make([]Tuple, 2)
	dp[0] = Tuple{1, nums[0]}
	dp[1] = Tuple{1, nums[0]}

	for i := 1; i < n; i++ {
		// dp[0] (Increase)
		var ti Tuple
		if dp[1].val < nums[i] {
			ti = Tuple{dp[1].num + 1, nums[i]}
		} else if dp[0].val < nums[i] {
			ti = Tuple{dp[0].num, nums[i]}
		} else {
			ti = dp[0]
		}

		// dp[1] (Decrease)
		var td Tuple
		if dp[0].val > nums[i] {
			td = Tuple{dp[0].num + 1, nums[i]}
		} else if dp[1].val > nums[i] {
			td = Tuple{dp[1].num, nums[i]}
		} else {
			td = dp[1]
		}

		dp[0] = ti
		dp[1] = td
	}

	result := dp[0].num
	if dp[1].num > result {
		result = dp[1].num
	}

	return result
}
