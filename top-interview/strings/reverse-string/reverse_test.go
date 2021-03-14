package reverse

import "testing"

func TestReverseString(t *testing.T) {
	var testCases = []struct {
		s    []byte
		want string
	}{
		{[]byte("hello"), "olleh"},
		{[]byte("Hannah"), "hannaH"},
	}
	for _, tc := range testCases {
		reverse(&tc.s)
		if string(tc.s) != tc.want {
			t.Errorf("reversString(%v) = %s, expected %s", tc.s, string(tc.s), tc.want)
		}
	}
}
