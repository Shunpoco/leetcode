package besttime

func maxProfit(prices []int) int {
	r := 0
	for i := 0; i < len(prices)-1; i++ {
		d := prices[i+1] - prices[i]

		if d > 0 {
			r += d
		}
	}

	return r
}
