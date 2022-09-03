package main

func numsSameConsecDiff(n int, k int) []int {
	result := []int{}
	memo := make(map[int][]int)
	for i := 1; i <= 9; i++ {
		solve(i, n-1, k, &result, &memo)
	}

	return result
}

func solve(digit, n, k int, result *[]int, memo *map[int][]int) {
	if n == 0 {
		(*result) = append(*result, digit)
		return
	}

	v := digit % 10
	if list, ok := (*memo)[v]; ok {
		for _, i := range list {
			solve(digit*10+i, n-1, k, result, memo)
		}
	} else {
		l := []int{}
		for i := 0; i <= 9; i++ {
			diff := v - i
			if diff < 0 {
				diff *= -1
			}
			if diff == k {
				l = append(l, i)
				solve(digit*10+i, n-1, k, result, memo)
			}
		}
		(*memo)[v] = l
	}
}
