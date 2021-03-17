package merge

func merge(nums1 []int, m int, nums2 []int, n int) {
	for i, val := range nums2 {
		idx := binarySearch(val, nums1[:m+i], 0)
		temp := append([]int{}, nums1[idx:]...)
		nums1[idx] = val
		nums1 = append(nums1[:idx+1], temp[:len(temp)-1]...)
	}
}

func binarySearch(n int, nums []int, start int) int {
	if len(nums) == 0 {
		return start
	}

	mid := len(nums) / 2

	if nums[mid] == n {
		return start + mid
	} else if nums[mid] > n {
		return binarySearch(n, nums[:mid], start)
	}
	return binarySearch(n, nums[mid+1:], start+mid+1)
}
