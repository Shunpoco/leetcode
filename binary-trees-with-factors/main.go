package main

import "sort"

const MOD = 1000000007

func numFactoredBinaryTrees(arr []int) int {
	sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })
	memo := make(map[int]int)

	result := 0
	for i, num := range arr {
		result += solve(num, i, &arr, &memo)
		result %= MOD
	}

	return result
}

func solve(num, idx int, arr *[]int, memo *map[int]int) int {
	if v := (*memo)[num]; v != 0 {
		return v
	}

	result := 1

	for i := 0; i < idx; i++ {
		v := (*arr)[i]
		if num%v == 0 {
			v2 := num / v
			if j := search(v2, (*arr)[:idx], 0); j != -1 {
				t1 := solve(v, i, arr, memo)
				t2 := solve(v2, j, arr, memo)
				a := t1 * t2
				a %= MOD

				result += a
				result %= MOD
			}
		}
	}

	(*memo)[num] = result

	return result
}

func search(num int, nums []int, start int) int {
	if len(nums) == 0 {
		return -1
	}

	m := len(nums) / 2

	v := nums[m]
	if v == num {
		return start + m
	} else if v > num {
		return search(num, nums[:m], start)
	} else {
		return search(num, nums[m+1:], start+m)
	}
}
