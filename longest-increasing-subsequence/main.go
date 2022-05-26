package main

func lengthOfLIS(nums []int) int {
	dp := []int{}

	for _, num := range nums {
		i := binary_search(dp, num, 0)
		if i >= len(dp) {
			dp = append(dp, num)
		} else {
			dp[i] = num
		}
	}

	// fmt.Println(dp)

	return len(dp)
}

func binary_search(nums []int, num int, start int) int {
	l := len(nums)
	if l == 0 {
		return start
	}

	m := l / 2

	v := nums[m]

	if v == num {
		return m + start
	} else if v > num {
		return binary_search(nums[:m], num, start)
	} else {
		return binary_search(nums[m+1:], num, start+m+1)
	}
}
