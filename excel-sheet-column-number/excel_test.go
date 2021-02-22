package excel

import "testing"

func TestTitleToNumber(t *testing.T) {
	var testCases = []struct {
		s    string
		want int
	}{
		{"A", 1},
		{"AB", 28},
		{"ZY", 701},
		{"AAA", 703},
		{"ZZ", 702},
		{"FXSHRXW", 2147483647},
	}

	for _, tc := range testCases {
		if r := titleToNumber(tc.s); r != tc.want {
			t.Errorf("titleToNumber(%s) = %d, expected %d", tc.s, r, tc.want)
		}
	}
}
