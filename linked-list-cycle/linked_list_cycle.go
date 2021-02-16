package linkedlist

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func hasCycle(head *ListNode) bool {
	if head == nil {
		return false
	}
	hash := map[string]int{}

	for head.Next != nil {
		key := fmt.Sprintf("%p", head)
		hash[key]++
		if hash[key] > 1 {
			return true
		}
		head = head.Next
	}

	return false
}
