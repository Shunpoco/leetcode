package main

func numOfMinutes(n int, headID int, manager []int, informTime []int) int {
	subordinates := make([][]int, n)

	for s, m := range manager {
		if m != -1 {
			subordinates[m] = append(subordinates[m], s)
		}
	}

	queue := make([][]int, 0, n)
	queue = append(queue, []int{headID, 0})
	var result = 0

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		if v[1] > result {
			result = v[1]
		}

		for _, sub := range subordinates[v[0]] {
			queue = append(queue, []int{sub, v[1] + informTime[v[0]]})
		}
	}

	return result
}
