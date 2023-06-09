package main

import "testing"

type test struct {
	letters []byte
	target  byte
	ideal   byte
}

func TestNextGreatestLetter(t *testing.T) {
	tests := []test{
		{[]byte("cfj"), byte('a'), byte('c')},
		{[]byte("cfj"), byte('c'), byte('f')},
		{[]byte("xxyyy"), byte('z'), byte('x')},
	}

	for i, test := range tests {
		actual := nextGreatestLetter(test.letters, test.target)
		if actual != test.ideal {
			t.Errorf("Case %d: nextGretestLetter(%x, %x) = %x should match %x", i, test.letters, test.target, actual, test.ideal)
		}
	}
}
