package cycle

import "testing"

func TestHasCycle(t *testing.T) {
	var testCases = []struct {
		head *ListNode
		want bool
	}{
		{makeCycle([]int{3, 2, 0, -4}, 1), true},
		{makeCycle([]int{1, 2}, 0), true},
		{&ListNode{1, nil}, false},
		{makeCycle([]int{-21, 10, 17, 8, 4, 26, 5, 35, 33, -7, -16, 27, -12, 6, 29, -12, 5, 9, 20, 14, 14, 2, 13, -24, 21, 23, -21, 5}, -1), false},
	}

	for _, tc := range testCases {
		if r := hasCycle(tc.head); r != tc.want {
			t.Errorf("hasCycle(%v) = %v, expected %v", tc.head, r, tc.want)
		}
	}

}

func makeCycle(nums []int, pos int) *ListNode {
	if len(nums) == 0 {
		return nil
	}
	root := &ListNode{nums[0], nil}
	joint := &ListNode{}
	if pos == 0 {
		joint = root
	}
	cur := root
	for i := 1; i < len(nums); i++ {
		cur.Next = &ListNode{nums[i], nil}
		cur = cur.Next
		if pos == i {
			joint = cur
		}
		if i == len(nums)-1 {
			cur.Next = joint
		}
	}

	return root
}
