package merge

import (
	"reflect"
	"testing"
)

func TestMergeTwoLists(t *testing.T) {
	var testCases = []struct {
		l1   []int
		l2   []int
		want []int
	}{
		{
			[]int{1, 2, 4},
			[]int{1, 3, 4},
			[]int{1, 1, 2, 3, 4, 4},
		},
		{[]int{}, []int{}, []int{}},
		{[]int{}, []int{0}, []int{0}},
	}

	for _, tc := range testCases {
		if r := toSlice(mergeTwoLists(toListNode(tc.l1), toListNode(tc.l2))); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("mergeTwoLists(%v, %v) = %v, expected %v", tc.l1, tc.l2, r, tc.want)
		}
	}
}

func toListNode(nums []int) *ListNode {
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
