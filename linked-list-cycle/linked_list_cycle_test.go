package linkedlist

import "testing"

func TestHasCycle(t *testing.T) {
	t10 := &ListNode{3, nil}
	t11 := &ListNode{2, nil}
	t12 := &ListNode{0, nil}
	t13 := &ListNode{-4, nil}
	t10.Next = t11
	t11.Next = t12
	t12.Next = t13
	t13.Next = t11

	t20 := &ListNode{1, nil}
	t21 := &ListNode{2, nil}
	t20.Next = t21
	t21.Next = t20

	var testCases = []struct {
		head *ListNode
		want bool
	}{
		{t10, true},
		{t20, true},
		{&ListNode{1, nil}, false},
	}

	for _, tc := range testCases {
		if r := hasCycle(tc.head); r != tc.want {
			t.Errorf("hasCycle(%v) = %v, expected %v", tc.head, r, tc.want)
		}
	}
}
