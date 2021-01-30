package removeDup

type ListNode struct {
	Val  int
	Next *ListNode
}

func deleteDuplicates(head *ListNode) *ListNode {
	if head == nil {
		return head
	}

	current := head
	next := head.Next
	for next != nil {
		if current.Val == next.Val {
			current.Next = next.Next
		} else {
			current = next
		}
		next = current.Next
	}
	return head
}
