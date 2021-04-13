package besttime

import "testing"

func TestMaxProfit(t *testing.T) {
	var testCases = []struct {
		prices []int
		want   int
	}{
		{
			[]int{7, 1, 5, 3, 6, 4},
			7,
		},
		{
			[]int{1, 2, 3, 4, 5},
			4,
		},
		{
			[]int{7, 6, 4, 3, 1},
			0,
		},
	}

	for idx, testCase := range testCases {
		if r := maxProfit(testCase.prices); r != testCase.want {
			t.Errorf("%d : %v, %d != %d", idx, testCase, r, testCase.want)
		}
	}
}
