package main

type Tuple struct {
	num int
	val int
}

func wiggleMaxLength(nums []int) int {
	n := len(nums)

	dp0 := Tuple{1, nums[0]}
	dp1 := Tuple{1, nums[0]}

	for i := 1; i < n; i++ {
		// dp0 (Increase)
		var ti Tuple
		if dp1.val < nums[i] {
			ti = Tuple{dp1.num + 1, nums[i]}
		} else if dp0.val < nums[i] {
			ti = Tuple{dp0.num, nums[i]}
		} else {
			ti = dp0
		}

		// dp1 (Decrease)
		var td Tuple
		if dp0.val > nums[i] {
			td = Tuple{dp0.num + 1, nums[i]}
		} else if dp1.val > nums[i] {
			td = Tuple{dp1.num, nums[i]}
		} else {
			td = dp1
		}

		dp0 = ti
		dp1 = td
	}

	result := dp0.num
	if dp1.num > result {
		result = dp1.num
	}

	return result
}
