package main

import "testing"

type test struct {
	nums  []int
	ideal int
}

func TestSemiOrderedPermutation(t *testing.T) {
	tests := []test{
		{
			[]int{2, 1, 4, 3},
			2,
		},
		{
			[]int{2, 4, 1, 3},
			3,
		},
		{
			[]int{1, 3, 4, 2, 5},
			0,
		},
	}

	for i, test := range tests {
		if actual := semiOrderedPermutation(test.nums); actual != test.ideal {
			t.Errorf("%d\n", i)
		}
	}
}
