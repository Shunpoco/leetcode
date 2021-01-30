package palindromeNumber

import "testing"

func TestIsPalindrome(t *testing.T) {
	testCases := []struct {
		x    int
		want bool
	}{
		{x: 121, want: true},
		{x: -121, want: false},
		{x: 10, want: false},
		{x: -101, want: false},
		{x: 123321, want: true},
	}

	for idx, testCase := range testCases {
		if isPalindrome(testCase.x) != testCase.want {
			t.Errorf("%d falied", idx)
		}
	}
}
