package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func partition(head *ListNode, x int) *ListNode {
	zero := ListNode{-201, head}
	prev := &zero

	cur := head

	for cur != nil && cur.Val < x {
		prev = cur
		cur = cur.Next
	}

	if cur == nil {
		return head
	}

	pp := cur
	prev2 := cur
	for cur != nil {
		if cur.Val < x {
			prev2.Next = cur.Next
			prev.Next = cur
			prev = cur
			prev.Next = pp

			cur = prev2.Next
		} else {
			prev2 = cur
			cur = cur.Next
		}
	}

	return zero.Next
}
