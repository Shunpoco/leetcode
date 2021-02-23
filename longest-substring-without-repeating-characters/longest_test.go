package longest

import "testing"

func TestLengthOfLongestSubstring(t *testing.T) {
	var testCases = []struct {
		s    string
		want int
	}{
		{"abcabcbb", 3},
		{"bbbbb", 1},
		{"pwwkew", 3},
		{"", 0},
		{"   ", 1},
		{"a12341", 5},
		{"dvdf", 3},
		{" ", 1},
		{"a", 1},
	}

	for _, tc := range testCases {
		if r := lengthOfLongestSubstring(tc.s); r != tc.want {
			t.Errorf("lengthOfLongestSubstring(%s) = %d, espected %d", tc.s, r, tc.want)
		}
	}
}
