package rotate

import (
	"reflect"
	"testing"
)

func TestRotate(t *testing.T) {
	var testCases = []struct {
		nums *[]int
		k    int
		want []int
	}{
		{
			&[]int{1, 2, 3, 4, 5, 6, 7},
			3,
			[]int{5, 6, 7, 1, 2, 3, 4},
		},
		{
			&[]int{-1, -100, 3, 99},
			2,
			[]int{3, 99, -1, -100},
		},
	}

	for _, tc := range testCases {
		if rotate(*tc.nums, tc.k); !reflect.DeepEqual(*tc.nums, tc.want) {
			t.Errorf("rotate = %v, expected %v", *tc.nums, tc.want)
		}
	}
}
