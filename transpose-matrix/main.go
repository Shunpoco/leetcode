package main

func transpose(matrix [][]int) [][]int {
	res := make([][]int, len(matrix[0]))
	for i := 0; i < len(res); i++ {
		res[i] = make([]int, len(matrix))
	}

	for c := 0; c < len(matrix[0]); c++ {
		for r := 0; r < len(matrix); r++ {
			res[c][r] = matrix[r][c]
		}
	}

	return res
}
