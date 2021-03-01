package cycle

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func detectCycle(head *ListNode) *ListNode {
	hash := map[string]int{}

	for {
		if head == nil {
			return nil
		}
		pointer := fmt.Sprintf("%p", head)
		hash[pointer]++
		if hash[pointer] == 2 {
			break
		}
		head = head.Next
	}

	return head
}
