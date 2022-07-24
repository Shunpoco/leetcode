package main

func searchMatrix(matrix [][]int, target int) bool {
	m := len(matrix)
	n := len(matrix[0])

	cur_row := 0
	cur_col := n - 1

	for cur_row < m && cur_col >= 0 {
		v := matrix[cur_row][cur_col]
		if v == target {
			return true
		} else if v > target {
			cur_col--
		} else {
			cur_row++
		}
	}

	return false
}
