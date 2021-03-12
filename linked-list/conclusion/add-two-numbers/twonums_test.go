package twonums

import (
	"reflect"
	"testing"
)

func TestAddTwoNumbers(t *testing.T) {
	var testCases = []struct {
		l1   []int
		l2   []int
		want []int
	}{
		{[]int{2, 4, 3}, []int{5, 6, 4}, []int{7, 0, 8}},
		{[]int{0}, []int{0}, []int{0}},
		{[]int{9, 9, 9, 9, 9, 9, 9}, []int{9, 9, 9, 9}, []int{8, 9, 9, 9, 0, 0, 0, 1}},
	}

	for _, tc := range testCases {
		if r := toSlice(addTwoNumbers(toListNode(tc.l1), toListNode(tc.l2))); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("addTwoNumbers(%v, %v) = %v, expected %v", tc.l1, tc.l2, r, tc.want)
		}
	}
}

func toSlice(head *ListNode) []int {
	r := []int{}

	for head != nil {
		r = append(r, head.Val)
		head = head.Next
	}

	return r
}

func toListNode(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	head := &ListNode{nums[0], nil}
	cur := head
	for i := 1; i < len(nums); i++ {
		n := &ListNode{nums[i], nil}
		cur.Next = n
		cur = cur.Next
	}

	return head
}
