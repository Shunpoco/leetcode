package odd

type ListNode struct {
	Val  int
	Next *ListNode
}

func oddEvenList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}
	count := 3
	oddT := head
	evenT := head.Next
	evenH := evenT
	cur := head.Next.Next
	for cur != nil {
		if count%2 != 0 {
			oddT.Next = cur
			cur = cur.Next
			oddT = oddT.Next
			oddT.Next = evenH
			evenT.Next = nil
		} else {
			evenT.Next = cur
			cur = cur.Next
			evenT = evenT.Next
			evenT.Next = nil
		}
		count++
	}
	return head
}
