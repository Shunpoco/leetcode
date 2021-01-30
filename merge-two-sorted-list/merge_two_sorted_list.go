package mergeTwo

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	var res *ListNode = &ListNode{}
	resCopy := res

	for {
		if l1 == nil && l2 == nil {
			break
		}
		if l1 == nil {
			resCopy.Next = l2
			l2 = l2.Next
			resCopy = resCopy.Next
			continue
		}
		if l2 == nil {
			resCopy.Next = l1
			l1 = l1.Next
			resCopy = resCopy.Next
			continue
		}
		if l1.Val >= l2.Val {
			resCopy.Next = l2
			l2 = l2.Next
			resCopy = resCopy.Next
			continue
		}
		if l1.Val < l2.Val {
			resCopy.Next = l1
			l1 = l1.Next
			resCopy = resCopy.Next
			continue
		}
	}
	return res.Next
}

// https://leetcode.com/problems/merge-two-sorted-lists/discuss/1007176/0-ms-Golang-solution からListNodeの扱い方についてヒントを得てしまったので忘れたころに追試したい
