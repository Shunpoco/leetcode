package main

type Position struct {
	row int
	col int
}

func maxAreaOfIsland(grid [][]int) int {
	m := len(grid)
	n := len(grid[0])
	visit := make([][]int, m)
	stack := []Position{}

	for i := 0; i < m; i++ {
		visit[i] = make([]int, n)
	}

	result := 0
	for row := 0; row < m; row++ {
		for col := 0; col < n; col++ {
			if grid[row][col] == 1 && visit[row][col] == 0 {
				v := 0
				stack = append(stack, Position{row, col})
				for len(stack) > 0 {
					cur := stack[len(stack)-1]
					stack = stack[:len(stack)-1]
					if grid[cur.row][cur.col] == 1 && visit[cur.row][cur.col] == 0 {
						visit[cur.row][cur.col] = 1
						v += 1
						if cur.row >= 1 {
							stack = append(stack, Position{cur.row - 1, cur.col})
						}
						if cur.row < m-1 {
							stack = append(stack, Position{cur.row + 1, cur.col})
						}
						if cur.col >= 1 {
							stack = append(stack, Position{cur.row, cur.col - 1})
						}
						if cur.col < n-1 {
							stack = append(stack, Position{cur.row, cur.col + 1})
						}
					}
				}
				if v > result {
					result = v
				}
			}
		}
	}

	// fmt.Println(visit)

	return result
}
