package main

import "testing"

func TestMyHashMap(t *testing.T) {
	hash := Constructor()

	hash.Put(1, 1)
	hash.Put(2, 2)

	v := hash.Get(1)
	if v != 1 {
		t.Errorf("v")
	}

	v = hash.Get(3)
	if v != -1 {
		t.Errorf("v")
	}

	hash.Put(2, 1)

	v = hash.Get(2)
	if v != 1 {
		t.Errorf("v")
	}

	hash.Remove(2)
	v = hash.Get(2)
	if v != -1 {
		t.Errorf("v")
	}
}
