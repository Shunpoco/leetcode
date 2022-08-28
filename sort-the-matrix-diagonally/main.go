package main

import "sort"

func diagonalSort(mat [][]int) [][]int {
	m := len(mat)
	n := len(mat[0])

	for i := 0; i < m; i++ {
		solve(i, 0, m, n, &mat)
	}

	for i := 1; i < n; i++ {
		solve(0, i, m, n, &mat)
	}

	return mat
}

func solve(row, col, m, n int, mat *[][]int) {
	arr := []int{}
	r := row
	c := col
	for r < m && c < n {
		arr = append(arr, (*mat)[r][c])
		r++
		c++
	}

	sort.Slice(arr, func(i, j int) bool { return arr[i] < arr[j] })

	r = row
	c = col
	i := 0
	for r < m && c < n {
		(*mat)[r][c] = arr[i]
		i++
		r++
		c++
	}
}
