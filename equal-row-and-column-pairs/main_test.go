package main

import "testing"

type test struct {
	grid  [][]int
	ideal int
}

func TestEqualPairs(t *testing.T) {
	tests := []test{
		{
			[][]int{
				{3, 2, 1},
				{1, 7, 6},
				{2, 7, 7},
			},
			1,
		},
		{
			[][]int{
				{3, 1, 2, 2},
				{1, 4, 4, 5},
				{2, 4, 2, 2},
				{2, 4, 2, 2},
			},
			3,
		},
	}

	for i, test := range tests {
		if actual := equalPairs(test.grid); actual != test.ideal {
			t.Errorf("%d\n", i)
		}
	}
}
