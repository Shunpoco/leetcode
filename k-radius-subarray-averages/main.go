package main

func getAverages(nums []int, k int) []int {
	n := len(nums)

	result := make([]int, n)
	for i := 0; i < n; i++ {
		result[i] = -1
	}

	if n < 2*k+1 {
		return result
	}

	var t int
	t = sum(nums[:2*k+1])
	result[k] = t / (2*k + 1)
	for i := 0; i < n-2*k-1; i++ {
		t = t - nums[i] + nums[2*k+1+i]
		result[k+i+1] = t / (2*k + 1)
	}

	return result
}

func sum(nums []int) int {
	var result int
	for _, num := range nums {
		result += num
	}

	return result
}
