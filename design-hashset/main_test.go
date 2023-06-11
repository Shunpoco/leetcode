package main

import "testing"

func TestMyHashSet(t *testing.T) {
	hash := Constructor()

	hash.Add(1)
	hash.Add(2)

	isC := hash.Contains(1)
	if !isC {
		t.Errorf("isC")
	}

	isC = hash.Contains(3)
	if isC {
		t.Errorf("isC")
	}

	hash.Add(2)
	hash.Remove(2)
	isC = hash.Contains(2)

	if isC {
		t.Errorf("isC")
	}
}
