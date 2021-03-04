package remove

import (
	"reflect"
	"testing"
)

func TestRemoveNthFromEnd(t *testing.T) {
	var testCases = []struct {
		head []int
		n    int
		want []int
	}{
		{[]int{1, 2, 3, 4, 5}, 2, []int{1, 2, 3, 5}},
		{[]int{1}, 1, []int{}},
		{[]int{1, 2}, 1, []int{1}},
		{[]int{1, 2}, 2, []int{2}},
	}

	for _, tc := range testCases {
		if r := fetchNumsFromLL(removeNthFromEnd(makeLinkedList(tc.head), tc.n)); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("removeNthFromEnd(%v, %d) = %v, expected %v", tc.head, tc.n, r, tc.want)
		}
	}
}

func makeLinkedList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	ll := &ListNode{nums[0], nil}
	cur := ll
	for i := 1; i < len(nums); i++ {
		node := &ListNode{nums[i], nil}
		cur.Next = node
		cur = cur.Next
	}

	return ll
}

func fetchNumsFromLL(head *ListNode) []int {
	nums := []int{}
	for head != nil {
		nums = append(nums, head.Val)
		head = head.Next
	}
	return nums
}
