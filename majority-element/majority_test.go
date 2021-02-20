package majority

import "testing"

func TestMajorityElement(t *testing.T) {
	var testCases = []struct {
		nums []int
		want int
	}{
		{[]int{3, 2, 3}, 3},
		{[]int{2, 2, 1, 1, 1, 2, 2}, 2},
	}

	for _, tc := range testCases {
		if r := majorityElement(tc.nums); r != tc.want {
			t.Errorf("majorityElement(%v) = %d, expected %d", tc.nums, r, tc.want)
		}
	}
}
