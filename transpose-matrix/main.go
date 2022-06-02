package main

func transpose(matrix [][]int) [][]int {
	res := make([][]int, len(matrix[0]))

	for c := 0; c < len(matrix[0]); c++ {
		for r := 0; r < len(matrix); r++ {
			res[c] = append(res[c], matrix[r][c])
		}
	}

	return res
}
