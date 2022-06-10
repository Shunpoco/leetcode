package main

func numSquares(n int) int {
	memory := make([]int, n+1)
	exec(n, &memory)

	return memory[n]
}

func exec(n int, memory *[]int) {
	if n == 0 || (*memory)[n] != 0 {
		return
	}

	result := n
	for num := 1; num*num <= n; num++ {
		t := n / (num * num)
		r := n - num*num*t
		exec(r, memory)
		t += (*memory)[r]

		if t < result {
			result = t
		}
	}

	(*memory)[n] = result
}
