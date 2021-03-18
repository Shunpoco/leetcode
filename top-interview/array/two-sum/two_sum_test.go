package twosum

import (
	"reflect"
	"testing"
)

func TestTwoSum(t *testing.T) {
	var testCases = []struct {
		nums   []int
		target int
		want   []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for _, tc := range testCases {
		if r := twoSum(tc.nums, tc.target); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("twoSum(%v, %d) = %v, expected %v", tc.nums, tc.target, r, tc.want)
		}
	}
}
