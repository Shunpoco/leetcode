package main

import "testing"

type input struct {
	prices []int
	fee    int
}

type test struct {
	name  string
	input input
	want  int
}

func TestMaxProfit(t *testing.T) {
	tests := []test{
		{
			name: "1",
			input: input{
				[]int{1, 3, 2, 8, 4, 9},
				2,
			},
			want: 8,
		},
		{
			name: "2",
			input: input{
				[]int{1, 3, 7, 5, 10, 3},
				3,
			},
			want: 6,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit(tt.input.prices, tt.input.fee); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
