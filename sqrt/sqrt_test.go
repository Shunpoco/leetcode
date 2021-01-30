package mySqrt

import "testing"

func TestMySqrt(t *testing.T) {
	var testCases = []struct {
		x        int
		expected int
	}{
		{x: 4, expected: 2},
		{x: 8, expected: 2},
		{x: 10000000, expected: 3162},
		{x: 0, expected: 0},
		{x: 1, expected: 1},
	}

	for idx, testCase := range testCases {
		if mySqrt(testCase.x) != testCase.expected {
			t.Errorf("%d: failed, %d, %d", idx, mySqrt(testCase.x), testCase.expected)
		}
	}
}
