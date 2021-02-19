package excel

import "testing"

func TestConvertToTitle(t *testing.T) {
	var testCases = []struct {
		n    int
		want string
	}{
		{1, "A"},
		{28, "AB"},
		{701, "ZY"},
	}

	for _, tc := range testCases {
		if r := convertToTitle(tc.n); r != tc.want {
			t.Errorf("convertToTitle(%d) = %s, expected %s", tc.n, r, tc.want)
		}
	}
}
