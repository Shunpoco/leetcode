package main

func longestIncreasingPath(matrix [][]int) int {
	m := len(matrix)
	n := len(matrix[0])

	memory := make([]int, m*n)

	var result int
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			t := dp(i, j, m, n, &matrix, &memory)
			if t > result {
				result = t
			}
		}
	}

	return result
}

func dp(row, col, m, n int, matrix *[][]int, memory *[]int) int {
	if v := (*memory)[row*n+col]; v != 0 {
		return v
	}

	val := (*matrix)[row][col]

	result := 1

	for _, i := range []int{-1, 1} {
		if row+i >= 0 && row+i < m && (*matrix)[row+i][col] > val {
			t := 1 + dp(row+i, col, m, n, matrix, memory)
			if t > result {
				result = t
			}
		}
		if col+i >= 0 && col+i < n && (*matrix)[row][col+i] > val {
			t := 1 + dp(row, col+i, m, n, matrix, memory)
			if t > result {
				result = t
			}
		}
	}

	(*memory)[row*n+col] = result

	return result
}
