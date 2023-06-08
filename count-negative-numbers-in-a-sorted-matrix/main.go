package main

import "fmt"

func countNegatives(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])

	var result int

	row := 0
	col := n - 1
	for row < m && col >= 0 {
		if grid[row][col] < 0 {
			result += m - row
			col--
		} else {
			row += 1
		}
	}

	return result
}

func main() {
	fmt.Println(countNegatives([][]int{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}}))
}
