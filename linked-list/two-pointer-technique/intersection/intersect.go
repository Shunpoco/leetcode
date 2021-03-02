package intersect

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func getIntersectionNode(headA, headB *ListNode) *ListNode {
	if headA == nil || headB == nil {
		return nil
	}
	hash := map[string]int{}

	a := headA
	for a != nil {
		pointer := fmt.Sprintf("%p", a)
		hash[pointer]++
		a = a.Next
	}

	b := headB
	for b != nil {
		pointer := fmt.Sprintf("%p", b)
		hash[pointer]++
		if hash[pointer] > 1 {
			return b
		}
		b = b.Next
	}
	return nil
}
