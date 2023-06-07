package main

import "testing"

func TestMinFlips(t *testing.T) {
	a := 2
	b := 6
	c := 5

	ideal := 3

	actual := minFlips(a, b, c)

	if actual != ideal {
		t.Fatalf("minFlips(%d, %d, %d) = %d want match for %d", a, b, c, actual, ideal)
	}
}
