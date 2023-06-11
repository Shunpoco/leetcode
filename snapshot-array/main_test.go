package main

import "testing"

func TestSnapshotArray(t *testing.T) {
	sa := Constructor(3)

	sa.Set(0, 5)
	id := sa.Snap()
	if id != 0 {
		t.Errorf("id does not 0: %d", id)
	}

	sa.Set(0, 6)

	v := sa.Get(0, 0)
	if v != 5 {
		t.Errorf("Value does not 5: %d", v)
	}
}
