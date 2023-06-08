package main

import "testing"

type test struct {
	grid  [][]int
	ideal int
}

func TestCountNegative(t *testing.T) {
	tests := []test{
		{
			grid:  [][]int{{4, 3, 2, -1}, {3, 2, 1, -1}, {1, 1, -1, -2}, {-1, -1, -2, -3}},
			ideal: 8,
		},
	}

	for i, test := range tests {
		actual := countNegatives(test.grid)

		if actual != test.ideal {
			t.Errorf("Case %d: countNegative(%x) = %d should match %d", i, test.grid, actual, test.ideal)
		}
	}
}
