package main

import "testing"

type test struct {
	name  string
	input []int
	want  int
}

func TestMaxProfit(t *testing.T) {
	tests := []test{
		{
			name:  "1",
			input: []int{7, 1, 5, 3, 6, 4},
			want:  7,
		},
		{
			name:  "2",
			input: []int{1, 2, 3, 4, 5},
			want:  4,
		},
		{
			name:  "3",
			input: []int{7, 6, 4, 3, 1},
			want:  0,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := maxProfit(tt.input); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
