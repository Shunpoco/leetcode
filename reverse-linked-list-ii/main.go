package main

// Definition for singly-linked list.
type ListNode struct {
	Val  int
	Next *ListNode
}

func reverseBetween(head *ListNode, left int, right int) *ListNode {
	root := &ListNode{-1, head}
	counter := 1
	cur := head
	before_left := root
	for counter < left {
		counter++
		before_left = cur
		cur = (*cur).Next
	}
	stack := []*ListNode{}
	for counter <= right {
		counter++
		stack = append(stack, cur)
		cur = (*cur).Next
	}

	after_right := cur
	prev := before_left
	for len(stack) > 0 {
		cur = stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		(*prev).Next = cur
		prev = cur
	}
	(*prev).Next = after_right

	return (*root).Next
}
