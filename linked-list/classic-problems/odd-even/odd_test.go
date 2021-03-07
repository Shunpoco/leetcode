package odd

import (
	"reflect"
	"testing"
)

func TestOddEvenList(t *testing.T) {
	var testCases = []struct {
		head []int
		want []int
	}{
		{[]int{1, 2, 3, 4, 5}, []int{1, 3, 5, 2, 4}},
		{[]int{2, 1, 3, 5, 6, 4, 7}, []int{2, 3, 6, 7, 1, 5, 4}},
		{[]int{}, []int{}},
		{[]int{1}, []int{1}},
	}

	for _, tc := range testCases {
		if r := toSlice(oddEvenList(toLinkedList(tc.head))); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("oddEvenList(%v) = %v, expected %v", tc.head, r, tc.want)
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
