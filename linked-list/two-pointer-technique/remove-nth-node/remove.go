package remove

// ListNode is the definitoin of each nodes in a linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func removeNthFromEnd(head *ListNode, n int) *ListNode {
	// Get Length of LL
	cur := head
	length := 0
	for cur != nil {
		length++
		cur = cur.Next
	}

	if length-n <= 0 {
		return head.Next
	}

	cur = head
	for i := 1; i < length-n; i++ {
		cur = cur.Next
	}
	if cur.Next != nil {
		cur.Next = cur.Next.Next
	}

	return head
}
