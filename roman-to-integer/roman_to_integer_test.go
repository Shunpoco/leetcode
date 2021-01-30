package romanToInt

import "testing"

func TestRomanToInt(t *testing.T) {
	testCases := []struct {
		s    string
		want int
	}{
		{s: "III", want: 3},
		{s: "IV", want: 4},
		{s: "IX", want: 9},
		{s: "LVIII", want: 58},
		{s: "MCMXCIV", want: 1994},
	}

	for idx, testCase := range testCases {
		if romanToInt(testCase.s) != testCase.want {
			t.Errorf("%d failed.\n", idx)
		}
	}
}
