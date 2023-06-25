package main

import "testing"

type test struct {
	name  string
	input struct {
		locations []int
		start     int
		finish    int
		fuel      int
	}
	want int
}

func TestCountRoutes(t *testing.T) {
	tests := []test{
		{
			name: "1",
			input: struct {
				locations []int
				start     int
				finish    int
				fuel      int
			}{
				locations: []int{2, 3, 6, 8, 4},
				start:     1,
				finish:    3,
				fuel:      5,
			},
			want: 4,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := countRoutes(tt.input.locations, tt.input.start, tt.input.finish, tt.input.fuel); got != tt.want {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
