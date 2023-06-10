package main

import "testing"

type test struct {
	words []string
	ideal string
}

func TestOddString(t *testing.T) {
	tests := []test{
		{
			[]string{"adc", "wzy", "abc"},
			"abc",
		},
		{
			[]string{"aaa", "bob", "ccc", "ddd"},
			"bob",
		},
	}

	for i, test := range tests {
		actual := oddString(test.words)

		if actual != test.ideal {
			t.Errorf("Case %d: oddString(%x) = %s should match %s", i, test.words, actual, test.ideal)
		}
	}
}
