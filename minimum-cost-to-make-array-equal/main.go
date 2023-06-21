package main

func minCost(nums []int, cost []int) int64 {
	left, right := min(nums), max(nums)+1

	var result int64

	for left < right {
		mid := (left + right) / 2
		c1 := calc(mid, nums, cost)
		c2 := calc(mid+1, nums, cost)

		if c1 > c2 {
			left = mid + 1
			result = c2
		} else {
			right = mid
			result = c1
		}
	}
	return result
}

func min(nums []int) int64 {
	r := nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] < r {
			r = nums[i]
		}
	}

	return int64(r)
}

func max(nums []int) int64 {
	r := nums[0]

	for i := 1; i < len(nums); i++ {
		if nums[i] > r {
			r = nums[i]
		}
	}

	return int64(r)
}

func abs(val int64) int64 {
	if val < 0 {
		return -val
	}

	return val
}

func calc(val int64, nums []int, cost []int) int64 {
	var r int64
	for i, num := range nums {
		r += int64(cost[i]) * abs(int64(num)-val)
	}

	return r
}
