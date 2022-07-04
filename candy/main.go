package main

func candy(ratings []int) int {
	n := len(ratings)
	order := make([]int, n)
	order[0] = 1
	order[n-1] = 1

	for i := 1; i < n; i++ {
		v := 1
		if ratings[i] > ratings[i-1] {
			v = order[i-1] + 1
		}
		if order[i] < v {
			order[i] = v
		}

		v = 1
		if ratings[n-1-i] > ratings[n-1-(i-1)] {
			v = order[n-1-(i-1)] + 1
		}
		if order[n-1-i] < v {
			order[n-1-i] = v
		}
	}

	var result int
	for _, num := range order {
		result += num
	}

	return result
}
