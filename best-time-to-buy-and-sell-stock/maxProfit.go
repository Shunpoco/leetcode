package max_profit

const MAX_VALUE = 10000

func maxProfit(prices []int) int {
	minPrice := MAX_VALUE
	profit := 0

	for i := 0; i < len(prices); i++ {
		if prices[i] < minPrice {
			minPrice = prices[i]
		} else if prices[i]-minPrice > profit {
			profit = prices[i] - minPrice
		}
	}

	return profit
}
