package twonums

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var result *ListNode
	var cur *ListNode

	carry := 0

	for l1 != nil || l2 != nil || carry != 0 {
		node, c := add(l1, l2, carry)

		if result == nil {
			result = node
		} else {
			cur.Next = node
		}
		cur = node

		if l1 != nil {
			l1 = l1.Next
		}
		if l2 != nil {
			l2 = l2.Next
		}
		carry = c
	}

	return result
}

func add(l1 *ListNode, l2 *ListNode, carry int) (*ListNode, int) {
	val1, val2 := 0, 0
	if l1 != nil {
		val1 = l1.Val
	}
	if l2 != nil {
		val2 = l2.Val
	}
	sum := val1 + val2 + carry
	carry = sum / 10
	val := sum % 10

	return &ListNode{val, nil}, carry
}
