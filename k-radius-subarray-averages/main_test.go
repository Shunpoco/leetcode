package main

import (
	"reflect"
	"testing"
)

type test struct {
	name  string
	input input
	want  []int
}

type input struct {
	nums []int
	k    int
}

func TestGetAverages(t *testing.T) {
	tests := []test{
		{
			name: "1",
			input: input{
				nums: []int{7, 4, 3, 9, 1, 8, 5, 2, 6},
				k:    3,
			},
			want: []int{-1, -1, -1, 5, 4, 4, -1, -1, -1},
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := getAverages(tt.input.nums, tt.input.k); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("%s", tt.name)
			}
		})
	}
}
