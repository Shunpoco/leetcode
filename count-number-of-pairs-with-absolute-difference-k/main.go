package main

import "fmt"

func countKDifference(nums []int, k int) int {
	result := 0

	hash := make(map[int]int, len(nums))

	for i := 0; i < len(nums); i++ {
		v := nums[i]
		sub := k + v
		sub2 := 0
		if k < v {
			sub2 = v - k
		}

		result += hash[sub]

		if sub2 > 0 {
			result += hash[sub2]
		}

		hash[v] += 1
	}

	return result
}

func main() {
	fmt.Println(countKDifference([]int{1, 2, 2, 1}, 1))
}
