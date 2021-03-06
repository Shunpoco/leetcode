package remove

type ListNode struct {
	Val  int
	Next *ListNode
}

func removeElements(head *ListNode, val int) *ListNode {
	if head == nil {
		return nil
	}

	cur := head
	var prev *ListNode

	for cur != nil {
		if cur.Val == val {
			if prev != nil {
				prev.Next = cur.Next
			} else {
				head = head.Next
			}
		} else {
			prev = cur
		}
		cur = cur.Next
	}

	return head
}
