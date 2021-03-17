package merge

func merge(nums1 []int, m int, nums2 []int, n int) {
	inner(&nums1, m, nums2, n)
}

func inner(nums1 *[]int, m int, nums2 []int, n int) {
	for _, val := range nums2 {
		idx := binarySearch(val, (*nums1)[:m], 0)
		*nums1 = append(append((*nums1)[:idx], val), (*nums1)[idx:]...)
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
