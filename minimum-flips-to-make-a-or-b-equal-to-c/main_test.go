package main

import "testing"

type test struct {
	a     int
	b     int
	c     int
	ideal int
}

func TestMinFlips(t *testing.T) {
	tests := []test{
		{2, 6, 5, 3},
		{4, 2, 7, 1},
		{1, 2, 3, 0},
		{2, 2, 1, 3},
	}

	for i, test := range tests {
		actual := minFlips(test.a, test.b, test.c)

		if actual != test.ideal {
			t.Errorf("Test case %d: minFlips(%d, %d, %d) = %d want match for %d", i+1, test.a, test.b, test.c, actual, test.ideal)
		}
	}
}
