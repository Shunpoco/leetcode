package merge

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	r := &ListNode{0, nil}
	c := r
	for l1 != nil || l2 != nil {
		if l1 != nil && l2 == nil {
			c.Next = &ListNode{l1.Val, nil}
			l1 = l1.Next
		} else if l1 == nil && l2 != nil {
			c.Next = &ListNode{l2.Val, nil}
			l2 = l2.Next
		} else {
			c1 := l1.Val
			c2 := l2.Val
			if c1 < c2 {
				c.Next = &ListNode{c1, nil}
				l1 = l1.Next
			} else {
				c.Next = &ListNode{c2, nil}
				l2 = l2.Next
			}
		}
		c = c.Next
	}

	return r.Next
}
