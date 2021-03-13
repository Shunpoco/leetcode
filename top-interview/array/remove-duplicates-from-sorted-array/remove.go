package remove

func removeDuplicates(nums []int) int {
	if len(nums) <= 1 {
		return len(nums)
	}
	current := nums[0]

	for i := 1; i < len(nums); {
		if current == nums[i] {
			nums = append(nums[:i], nums[i+1:]...)
		} else {
			current = nums[i]
			i++
		}
	}

	return len(nums)
}
