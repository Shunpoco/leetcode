package linkedlist

import (
	"testing"
)

func TestLinkedList(t *testing.T) {
	ll := Constructor()

	if ll.root != nil || ll.length != 0 {
		t.Errorf("Failed to initalize.")
	}

	ll.AddAtHead(1)
	ll.AddAtTail(3)
	ll.AddAtIndex(1, 2)

	want := []int{1, 2, 3}

	n := ll.root
	for i := 0; i < ll.length; i++ {
		if n.val != want[i] {
			t.Errorf("%d != %d", n.val, want[i])
		}
		n = n.next
	}

	if r := ll.Get(2); r != 3 {
		t.Errorf("Get: %d != %d", r, 3)
	}

	ll.DeleteAtIndex(0)
	ll.DeleteAtIndex(0)
	ll.DeleteAtIndex(0)
	if r := ll.Get(2); r != -1 {
		t.Errorf("Get: %d != %d", r, -1)
	}

}

func TestLinkedList2(t *testing.T) {
	ll := Constructor()

	ll.AddAtHead(7)
	ll.AddAtHead(2)
	ll.AddAtHead(1)
	ll.AddAtIndex(3, 0)
	ll.DeleteAtIndex(2)
	ll.AddAtHead(6)
	ll.AddAtTail(4)
	if ll.Get(4) != 4 {
		t.Errorf("%d != 4", ll.Get(4))
	}
	ll.AddAtHead(4)
	ll.AddAtIndex(5, 0)
	ll.AddAtHead(6)
}
