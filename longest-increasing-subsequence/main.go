package main

func lengthOfLIS(nums []int) int {
	arr := []int{}

	for _, num := range nums {
		if idx := binary_search(num, arr, 0); idx == len(arr) {
			arr = append(arr, num)
		} else {
			arr[idx] = num
		}
	}

	return len(arr)
}

func binary_search(num int, nums []int, start int) int {
	l := len(nums)
	if l == 0 {
		return start
	}

	m := l / 2
	v := nums[m]

	switch {
	case v > num:
		return binary_search(num, nums[:m], start)
	case v < num:
		return binary_search(num, nums[m+1:], start+m+1)
	default:
		return m + start
	}
}
