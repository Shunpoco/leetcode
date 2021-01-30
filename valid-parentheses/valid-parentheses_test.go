package validParentheses

import "testing"

func TestIsValid(t *testing.T) {
	testCases := []struct {
		s    string
		want bool
	}{
		{s: "()", want: true},
		{s: "()[]{}", want: true},
		{s: "(]", want: false},
		{s: "([)]", want: false},
		{s: "{[]}", want: true},
		{s: "[", want: false},
		{s: "}", want: false},
	}

	for idx, testCase := range testCases {
		if isValid(testCase.s) != testCase.want {
			t.Errorf("%d failed.", idx)
		}
	}
}
