package main

func findCircleNum(isConnected [][]int) int {
	n := len(isConnected)

	visited := make([]bool, n)

	var result int

	for i := 0; i < n; i++ {
		if visited[i] {
			continue
		}
		visited[i] = true
		queue := make([]int, 0, n)
		queue = append(queue, i)
		result++
		for len(queue) > 0 {
			v := queue[0]
			queue = queue[1:]

			for j, connected := range isConnected[v] {
				if connected == 1 && !visited[j] {
					visited[j] = true
					queue = append(queue, j)
				}
			}
		}
	}

	return result
}
