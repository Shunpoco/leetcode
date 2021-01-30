package twoSum

import "testing"

func TestTwosum(t *testing.T) {
	testCases := []struct {
		nums   []int
		target int
		want   []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
		{[]int{-1, 10, 9, 7}, 6, []int{0, 3}},
		{[]int{0, 0, 10, 12}, 0, []int{0, 1}},
	}

	for idx, testCase := range testCases {
		got := twoSum(testCase.nums, testCase.target)
		if !(compareArrays(got, testCase.want)) {
			t.Errorf("%d fali: expected is {%d, %d}, but actually {%d, %d}", idx, testCase.want[0], testCase.want[1], got[0], got[1])
		}
	}
}

func compareArrays(a []int, b []int) bool {
	if (a[0] == b[0] && a[1] == b[1]) || (a[1] == b[0] && a[0] == b[1]) {
		return true
	}
	return false
}
