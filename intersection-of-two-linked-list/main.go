package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	curA := headA
	lenA := 0
	for curA != nil {
		lenA++
		curA = (*curA).Next
	}

	curB := headB
	lenB := 0
	for curB != nil {
		lenB++
		curB = (*curB).Next
	}

	curA = headA
	curB = headB

	for lenA > lenB {
		curA = (*curA).Next
		lenA--
	}

	for lenB > lenA {
		curB = (*curB).Next
		lenB--
	}

	for curA != nil && curB != nil {
		if curA == curB {
			return curA
		}
		curA = (*curA).Next
		curB = (*curB).Next
	}

	return nil
}
