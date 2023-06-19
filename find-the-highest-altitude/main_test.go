package main

import "testing"

type test struct {
	name  string
	input []int
	want  int
}

func TestLargestAltitude(t *testing.T) {
	tests := []test{
		{
			"1",
			[]int{-5, 1, 5, 0, -7},
			1,
		},
		{
			"2",
			[]int{-4, -3, -2, -1, 4, 3, 2},
			0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := largestAltitude(tt.input); got != tt.want {
				t.Errorf("%s: %d != %d", tt.name, got, tt.want)
			}
		})
	}
}
