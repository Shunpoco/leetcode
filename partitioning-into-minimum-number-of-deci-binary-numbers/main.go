package main

import "strconv"

func minPartitions(n string) int {
	result := 0
	for _, num := range n {
		i, _ := strconv.Atoi(string(num))
		if i > result {
			result = i
		}
	}

	return result
}
