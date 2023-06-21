package main

import "testing"

type input struct {
	nums []int
	cost []int
}

type test struct {
	name  string
	input input
	want  int64
}

func TestMinCost(t *testing.T) {
	tests := []test{
		{
			name: "1",
			input: input{
				nums: []int{1, 3, 5, 2},
				cost: []int{2, 3, 1, 14},
			},
			want: 8,
		},
		{
			name: "2",
			input: input{
				nums: []int{2, 2, 2, 2, 2},
				cost: []int{4, 2, 8, 1, 3},
			},
			want: 0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := minCost(tt.input.nums, tt.input.cost); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
