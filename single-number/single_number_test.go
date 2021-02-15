package singleNumber

import "testing"

func TestSingleNumber(t *testing.T) {
	var testCases = []struct {
		nums []int
		want int
	}{
		{[]int{2, 2, 1}, 1},
		{[]int{4, 1, 2, 1, 2}, 4},
		{[]int{1}, 1},
	}

	for _, tc := range testCases {
		if r := singleNumber2(tc.nums); r != tc.want {
			t.Errorf("singleNumber(%v) = %d, expected %d", tc.nums, r, tc.want)
		}
	}
}
