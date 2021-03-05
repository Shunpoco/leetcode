package reverse

import (
	"reflect"
	"testing"
)

func TestReverseList(t *testing.T) {
	var testCases = []struct {
		head []int
		want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{5, 4, 3, 2, 1}},
		{[]int{1, 2}, []int{2, 1}},
		{[]int{}, []int{}},
	}

	for _, tc := range testCases {
		if r := toSlice(reverseList(toLinkedList(tc.head))); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("reverseList(%v) = %v, expected %v", tc.head, r, tc.want)
		}
	}
}

func toLinkedList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	r := &ListNode{nums[0], nil}
	cur := r
	for i := 1; i < len(nums); i++ {
		n := &ListNode{nums[i], nil}
		cur.Next = n
		cur = cur.Next
	}

	return r
}

func toSlice(head *ListNode) []int {
	r := []int{}

	for head != nil {
		r = append(r, head.Val)
		head = head.Next
	}

	return r
}
