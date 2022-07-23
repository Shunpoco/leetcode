package main

func countSmaller(nums []int) []int {
	n := len(nums)

	enumes := make([][]int, n)
	for i, v := range nums {
		enumes[i] = []int{i, v}
	}
	result := make([]int, n)

	sort(enumes, &result)

	return result
}

func sort(enumes [][]int, result *[]int) [][]int {
	n := len(enumes)
	mid := n / 2

	if mid > 0 {
		left, right := sort(enumes[:mid], result), sort(enumes[mid:], result)

		for i := n - 1; i >= 0; i-- {
			if len(right) == 0 || len(left) > 0 && left[len(left)-1][1] > right[len(right)-1][1] {
				(*result)[left[len(left)-1][0]] += len(right)
				enumes[i] = left[len(left)-1]
				left = left[:len(left)-1]
			} else {
				enumes[i] = right[len(right)-1]
				right = right[:len(right)-1]
			}
		}
	}

	r := make([][]int, n)
	copy(r, enumes)

	return r
}
