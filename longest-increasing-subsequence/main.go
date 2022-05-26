package main

func lengthOfLIS(nums []int) int {
	dp := []int{}

	for _, num := range nums {
		i := binary_search(num, dp, 0)
		if i >= len(dp) {
			dp = append(dp, num)
		} else {
			dp[i] = num
		}
	}

	return len(dp)
}

func binary_search(num int, nums []int, start int) int {
	l := len(nums)
	if l == 0 {
		return start
	}

	m := l / 2
	v := nums[m]

	switch {
	case v > num:
		return binary_search(num, nums[:m], start)
	case v < num:
		return binary_search(num, nums[m+1:], start+m+1)
	default:
		return m + start
	}
}
