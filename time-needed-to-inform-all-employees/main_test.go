package main

import "testing"

type test struct {
	n          int
	headID     int
	manager    []int
	informTime []int
	ideal      int
}

func TestNumOfMinutes(t *testing.T) {
	tests := []test{
		{1, 0, []int{-1}, []int{0}, 0},
		{6, 2, []int{2, 2, -1, 2, 2, 2}, []int{0, 0, 1, 0, 0, 0}, 1},
	}

	for i, test := range tests {
		actual := numOfMinutes(test.n, test.headID, test.manager, test.informTime)

		if actual != test.ideal {
			t.Errorf("Case %d: numOfMinutes(%d, %d, %x, %x) = %d should match %d", i, test.n, test.headID, test.manager, test.informTime, actual, test.ideal)
		}
	}
}
