package max_profit

import "testing"

func TestMaxProfit(t *testing.T) {
	var testCases = []struct {
		prices []int
		want   int
	}{
		{[]int{7, 1, 5, 3, 6, 4}, 5},
		{[]int{7, 6, 4, 3, 1}, 0},
	}

	for _, tc := range testCases {
		if r := maxProfit(tc.prices); r != tc.want {
			t.Errorf("maxProfit(%v) = %d, expected %d", tc.prices, r, tc.want)
		}
	}
}
