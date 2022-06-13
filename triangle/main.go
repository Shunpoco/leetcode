package main

type Position struct {
	Row   int
	Colum int
}

func minimumTotal(triangle [][]int) int {
	memory := make(map[Position]int)

	return solve(0, 0, &triangle, &memory)
}

func solve(row, column int, triangle *[][]int, memory *map[Position]int) int {
	if v, ok := (*memory)[Position{row, column}]; ok {
		return v
	}

	v := (*triangle)[row][column]
	result := v
	if row+1 < len(*triangle) {
		modify := false
		n := len((*triangle)[row+1])
		for i := 0; i < 2; i++ {
			if column+i < n {
				t := v + solve(row+1, column+i, triangle, memory)
				if !modify || result > t {
					result = t
					modify = true
				}
			}
		}
	}

	(*memory)[Position{row, column}] = result

	return result
}

// Use BFS but very slow
// type Position struct {
// 	Row    int
// 	Column int
// 	Val    int
// }

// func minimumTotal(triangle [][]int) int {
// 	memory := make(map[Position]int)
// 	queue := []Position{{0, 0, triangle[0][0]}}
// 	result := 10001
// 	for len(queue) > 0 {
// 		p := queue[0]
// 		queue = queue[1:]
// 		if p.Row+1 < len(triangle) {
// 			for i := 0; i < 2; i++ {
// 				if v, ok := memory[Position{p.Row + 1, p.Column + i, 0}]; !ok || v > p.Val+triangle[p.Row+1][p.Column+i] {
// 					memory[Position{p.Row + 1, p.Column + i, 0}] = p.Val + triangle[p.Row+1][p.Column+i]
// 					queue = append(queue, Position{p.Row + 1, p.Column + i, p.Val + triangle[p.Row+1][p.Column+i]})
// 				}
// 			}
// 		} else if p.Val < result {
// 			result = p.Val
// 		}
// 	}

// 	return result
// }
