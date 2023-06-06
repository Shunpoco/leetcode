package main

type Pos struct {
	x int
	y int
}

func shortestPathBinaryMatrix(grid [][]int) int {
	n := len(grid)

	queue := make([]Pos, n*n)
	score := make([][]int, n)
	for i := 0; i < n; i++ {
		score[i] = make([]int, n)
	}
	score[0][0] = 1

	// fmt.Println(score)

	for len(queue) > 0 {
		pos := queue[0]
		queue = queue[1:]

		if grid[pos.x][pos.y] == 1 {
			score[pos.x][pos.y] = -1
			continue
		}

		v := score[pos.x][pos.y]

		for _, i := range []int{-1, 0, 1} {
			for _, j := range []int{-1, 0, 1} {
				if pos.x+i >= 0 && pos.x+i < n && pos.y+j >= 0 && pos.y+j < n {
					if score[pos.x+i][pos.y+j] == -1 {
						continue
					}

					if score[pos.x+i][pos.y+j] == 0 || score[pos.x+i][pos.y+j] > v+1 {
						score[pos.x+i][pos.y+j] = v + 1
						queue = append(queue, Pos{pos.x + i, pos.y + j})
					}
				}
			}
		}

	}

	r := score[n-1][n-1]
	if r == 0 {
		return -1
	}
	return r
}

func shortestPathBinaryMatrix2(grid [][]int) int {
	n := len(grid)
	if grid[0][0] == 1 || grid[n-1][n-1] == 1 {
		return -1
	}

	queue := [][]int{{0, 0, 1}}
	grid[0][0] = 1

	for len(queue) > 0 {
		vs := queue[0]
		queue = queue[1:]

		if vs[0] == n-1 && vs[1] == n-1 {
			return vs[2]
		}

		for _, dx := range []int{-1, 0, 1} {
			for _, dy := range []int{-1, 0, 1} {
				nx := vs[0] + dx
				ny := vs[1] + dy

				if nx >= 0 && nx < n && ny >= 0 && ny < n && grid[nx][ny] != 1 {
					queue = append(queue, []int{nx, ny, vs[2] + 1})
					grid[nx][ny] = 1
				}
			}
		}
	}

	return -1
}
