package pascal

func generate(numRows int) [][]int {
	result := make([][]int, numRows)
	t := []int{}
	for i := 1; i <= numRows; i++ {
		t = solve(i, t)
		result[i-1] = t
	}

	return result
}

func solve(i int, t []int) []int {
	r := make([]int, i)
	r[0], r[i-1] = 1, 1

	for j := 1; j < i-1; j++ {
		r[j] = t[j-1] + t[j]
	}

	return r
}
