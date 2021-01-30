package searchInsert

func searchInsert(nums []int, target int) int {
	return compareCenter(nums, target, 0)
}

func compareCenter(nums []int, target int, sIdx int) int {
	lNums := len(nums)
	if lNums == 0 {
		return sIdx
	}
	cIdx := (lNums / 2)
	cVal := nums[cIdx]

	if target == cVal {
		return sIdx + cIdx
	}

	newNums := []int{}
	if target > cVal {
		if cIdx+1 < lNums {
			newNums = nums[cIdx+1:]
		}
		return compareCenter(newNums, target, sIdx+cIdx+1)
	}

	if cIdx != 0 {
		newNums = nums[:cIdx]
	}
	return compareCenter(newNums, target, sIdx)
}
