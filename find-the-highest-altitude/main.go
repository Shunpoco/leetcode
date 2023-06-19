package main

func largestAltitude(gain []int) int {
	n := len(gain)
	var result int
	var sum int
	for i := 0; i < n; i++ {
		sum += gain[i]
		if sum > result {
			result = sum
		}
	}

	return result
}
