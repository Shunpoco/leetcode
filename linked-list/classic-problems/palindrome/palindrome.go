package palindrome

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func isPalindrome(head *ListNode) bool {
	if head == nil {
		return false
	}
	// measure length
	cur := head
	length := 0
	for cur != nil {
		length++
		cur = cur.Next
	}
	firstEnd := length/2 - 1
	secondStart := length / 2
	if length%2 != 0 {
		secondStart++
	}

	first := ""
	second := ""
	cur = head
	for i := 0; i < length; i++ {
		if i <= firstEnd {
			first = fmt.Sprint(cur.Val) + first
		} else if i >= secondStart {
			second = second + fmt.Sprint(cur.Val)
		}
		cur = cur.Next
	}

	return first == second
}
