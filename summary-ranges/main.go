package main

import (
	"fmt"
	"strconv"
)

func summaryRanges(nums []int) []string {
	n := len(nums)
	result := make([]string, 0, n)
	if n == 0 {
		return result
	}

	left, right := 0, 0
	prev := nums[left]
	for i := 1; i < n; i++ {
		if nums[i] == prev+1 {
			right = i
		} else {
			if left == right {
				result = append(result, strconv.Itoa(nums[left]))
			} else {
				result = append(result, fmt.Sprintf("%d->%d", nums[left], nums[right]))
			}
			left, right = i, i
		}
		prev = nums[i]
	}

	if left == right {
		result = append(result, strconv.Itoa(nums[left]))
	} else {
		result = append(result, fmt.Sprintf("%d->%d", nums[left], nums[right]))
	}

	return result
}
