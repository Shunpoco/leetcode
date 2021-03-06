package remove

import (
	"reflect"
	"testing"
)

func TestRemoveLinkedLists(t *testing.T) {
	var testCases = []struct {
		head []int
		val  int
		want []int
	}{
		{[]int{1, 2, 6, 3, 4, 5, 6}, 6, []int{1, 2, 3, 4, 5}},
		{[]int{5, 5, 5, 5, 5, 2}, 5, []int{2}},
		{[]int{}, 2, []int{}},
	}

	for _, tc := range testCases {
		if r := toSlice(removeElements(toLinkedList(tc.head), tc.val)); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("removeElements(%v, %d) = %v, expected %v", tc.head, tc.val, r, tc.want)
		}
	}
}

func toLinkedList(nums []int) *ListNode {
	if len(nums) == 0 {
		return nil
	}

	r := &ListNode{nums[0], nil}
	c := r
	for i := 1; i < len(nums); i++ {
		n := &ListNode{nums[i], nil}
		c.Next = n
		c = c.Next
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
