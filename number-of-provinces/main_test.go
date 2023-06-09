package main

import "testing"

type test struct {
	isConnected [][]int
	ideal       int
}

func TestFindCircleNum(t *testing.T) {
	tests := []test{
		{
			[][]int{{1, 1, 0}, {1, 1, 0}, {0, 0, 1}},
			2,
		},
		{
			[][]int{{1, 0, 0}, {0, 1, 0}, {0, 0, 1}},
			3,
		},
	}

	for i, test := range tests {
		actual := findCircleNum(test.isConnected)

		if actual != test.ideal {
			t.Errorf("Case %d: findCircleNum(%x) = %d should match %d", i, test.isConnected, actual, test.ideal)
		}
	}
}
