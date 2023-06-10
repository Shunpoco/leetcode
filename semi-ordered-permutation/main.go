package main

func semiOrderedPermutation(nums []int) int {
	n := len(nums)

	var idx1 int
	var idxn int

	for i := 0; i < n; i++ {
		if nums[i] == 1 {
			idx1 = i
		} else if nums[i] == n {
			idxn = i
		}
	}

	result := idx1 + (n - 1 - idxn)

	if idxn < idx1 {
		result--
	}

	return result
}
