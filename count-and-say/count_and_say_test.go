package countAndSay

import "testing"

func TestCountAndSay(t *testing.T) {
	testCases := []struct {
		n        int
		expected string
	}{
		{n: 1, expected: "1"},
		{n: 4, expected: "1211"},
	}

	for idx, testCase := range testCases {
		if countAndSay(testCase.n) != testCase.expected {
	v		t.Errorf("%d: %s", idx, testCase.expected)
		}
	}
}
