package main

import "testing"

type test struct {
	nums  []int
	ideal bool
}

func TestFindSubarrays(t *testing.T) {
	tests := []test{
		{
			[]int{4, 2, 4},
			true,
		},
		{
			[]int{1, 2, 3, 4, 5},
			false,
		},
		{
			[]int{0, 0, 0},
			true,
		},
	}

	for i, test := range tests {
		actual := findSubarrays(test.nums)
		if actual != test.ideal {
			t.Errorf("%d\n", i)
		}
	}
}
