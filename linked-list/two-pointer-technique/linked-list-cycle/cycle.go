package cycle

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	// Two-pointer in Linked List
	if head == nil {
		return false
	}
	one := head
	two := head
	for i := 0; i < 10000; i++ {
		one = one.Next
		two = two.Next
		if one == nil || two == nil || two.Next == nil {
			return false
		}
		two = two.Next
		if one == two {
			return true
		}
	}
	return false
}
