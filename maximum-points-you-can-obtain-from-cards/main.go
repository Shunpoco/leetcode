package main

func maxScore(cardPoints []int, k int) int {
	n := len(cardPoints)
	sums := make([]int, k+1)

	sl := 0
	sr := 0
	for i := 0; i < k; i++ {
		sl += cardPoints[i]
		sr += cardPoints[n-1-i]
		sums[i+1] += sl
		sums[k+1-1-(i+1)] += sr
	}

	result := 0
	for i := 0; i < k+1; i++ {
		if sums[i] > result {
			result = sums[i]
		}
	}

	return result
}
