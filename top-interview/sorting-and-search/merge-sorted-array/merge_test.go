package merge

import (
	"reflect"
	"testing"
)

func TestInnerMerge(t *testing.T) {
	var testCases = []struct {
		nums1 []int
		m     int
		nums2 []int
		n     int
		want  []int
	}{
		{
			[]int{1, 2, 3, 0, 0, 0}, 3, []int{2, 5, 6}, 3,
			[]int{1, 2, 2, 3, 5, 6},
		},
		{
			[]int{1}, 1, []int{}, 0,
			[]int{1},
		},
	}

	for _, tc := range testCases {
		if merge2(&tc.nums1, tc.m, tc.nums2, tc.n); !reflect.DeepEqual(tc.nums1, tc.want) {
			t.Errorf("inner = %v, expected %v", tc.nums1, tc.want)
		}
	}
}
