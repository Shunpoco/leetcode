package climbingStairs

import "testing"

func TestClimbStairs(t *testing.T) {
	testCases := []struct {
		n        int
		expected int
	}{
		{n: 2, expected: 2},
		{n: 3, expected: 3},
	}

	for idx, testCase := range testCases {
		a := climbStairs(testCase.n)
		if a != testCase.expected {
			t.Errorf("%d faile: %d != %d", idx, a, testCase.expected)
		}
	}
}
