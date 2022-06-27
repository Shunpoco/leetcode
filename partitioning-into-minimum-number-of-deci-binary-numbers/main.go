package main

import "strconv"

func minPartitions(n string) int {
	result := "0"
	for _, num := range n {
		i := string(num)
		if i > result {
			result = i
		}
	}

	r, _ := strconv.Atoi(result)
	return r
}
