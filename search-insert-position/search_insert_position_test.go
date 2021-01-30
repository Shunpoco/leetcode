package searchInsert

import "testing"

func TestSearchInsert(t *testing.T) {
	testCases := []struct {
		nums     []int
		target   int
		expected int
	}{
		{
			nums:     []int{1, 3, 5, 6},
			target:   5,
			expected: 2,
		},
		{
			nums:     []int{1, 3, 5, 6},
			target:   2,
			expected: 1,
		},
		{
			nums:     []int{1, 3, 5, 6},
			target:   0,
			expected: 0,
		},
		{
			nums:     []int{1, 3, 5, 6},
			target:   7,
			expected: 4,
		},
	}

	for idx, testCase := range testCases {
		if searchInsert(testCase.nums, testCase.target) != testCase.expected {
			t.Errorf("%d failed.\n", idx)
		}
	}
}
