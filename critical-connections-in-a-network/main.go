package main

func criticalConnections(n int, connections [][]int) [][]int {
	var res [][]int

	graph := make([][]int, n)
	for _, c := range connections {
		graph[c[0]] = append(graph[c[0]], c[1])
		graph[c[1]] = append(graph[c[1]], c[0])
	}

	visited := make([]bool, n)
	lowlink := make([]int, n)
	counter := 0

	dfs(graph, -1, 0, &counter, &visited, &res, &lowlink)

	return res
}

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func dfs(graph [][]int, parent, node int, counter *int, visited *[]bool, res *[][]int, lowlink *[]int) {
	(*visited)[node] = true
	*counter++

	curlink := *counter
	(*lowlink)[node] = *counter
	for _, neighbor := range graph[node] {
		if neighbor == parent {
			continue
		}
		if !(*visited)[neighbor] {
			dfs(graph, node, neighbor, counter, visited, res, lowlink)
		}

		(*lowlink)[node] = min((*lowlink)[node], (*lowlink)[neighbor])

		if curlink < (*lowlink)[neighbor] {
			*res = append(*res, []int{node, neighbor})
		}
	}
}
