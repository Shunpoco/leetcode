package rotate

func rotate(nums []int, k int) {
	for i := 0; i < k; i++ {
		t := nums[len(nums)-1]
		copy(nums[1:], nums[0:len(nums)-1])
		nums[0] = t
	}
}
