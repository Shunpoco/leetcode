package number

import "testing"

func TestHammingWeight(t *testing.T) {
	var testCases = []struct {
		n    uint32
		want int
	}{
		{11, 3},
		{128, 1},
		{4294967293, 31},
	}

	for _, tc := range testCases {
		if r := hammingWeight(tc.n); r != tc.want {
			t.Errorf("hammingWeight(%d) = %d, expected %d", tc.n, r, tc.want)
		}
	}
}
