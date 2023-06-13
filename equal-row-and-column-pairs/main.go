package main

import "strconv"

func equalPairs(grid [][]int) int {
	n := len(grid)
	mem := make(map[string]int)

	for i := 0; i < n; i++ {
		t := ""
		for j := 0; j < n; j++ {
			t += strconv.Itoa(grid[i][j]) + ":"
		}
		mem[t]++
	}

	var result int
	for j := 0; j < n; j++ {
		t := ""
		for i := 0; i < n; i++ {
			t += strconv.Itoa(grid[i][j]) + ":"
		}
		result += mem[t]
	}

	return result
}
