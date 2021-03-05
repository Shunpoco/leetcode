package reverse

type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseList(head *ListNode) *ListNode {
	if head == nil {
		return nil
	}
	tail := head
	for tail.Next != nil {
		node := tail.Next
		tail.Next = node.Next
		node.Next = head
		head = node
	}

	return head
}
