package intersect

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}

	// Firstly, get lengths of headA and headB.
	lA, lB := 0, 0
	curA := headA
	curB := headB
	for curA != nil || curB != nil {
		if curA != nil {
			lA++
			curA = curA.Next
		}
		if curB != nil {
			lB++
			curB = curB.Next
		}
	}

	curA = headA
	curB = headB
	if lA > lB {
		return fetch(curA, curB, lA, lB)
	}
	return fetch(curB, curA, lB, lA)
}

// l1 is larger or equal than l2
func fetch(n1, n2 *ListNode, l1, l2 int) *ListNode {
	diff := l1 - l2

	for i := 0; i < diff; i++ {
		n1 = n1.Next
	}

	for n1 != nil && n2 != nil {
		if n1 == n2 {
			return n1
		}
		n1 = n1.Next
		n2 = n2.Next
	}

	return nil
}
