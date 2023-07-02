package main

import "testing"

type test struct {
	name     string
	n        int
	requests [][]int
	want     int
}

func TestMaximumRequests(t *testing.T) {
	tests := []test{
		{
			name: "1",
			n:    5,
			requests: [][]int{
				[]int{0, 1},
				[]int{1, 0},
				[]int{0, 1},
				[]int{1, 2},
				[]int{2, 0},
				[]int{3, 4},
			},
			want: 5,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maximumRequests(tt.n, tt.requests); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
