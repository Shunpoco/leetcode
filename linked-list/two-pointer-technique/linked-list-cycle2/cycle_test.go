package cycle

import "testing"

func TestDetectCycle(t *testing.T) {
	var testCases = []struct {
		head *ListNode
		want *ListNode
	}{
		{makeCycle([]int{3, 2, 0, 4}, 1), &ListNode{2, nil}},
		{makeCycle([]int{1, 2}, 0), &ListNode{1, nil}},
		{&ListNode{1, nil}, nil},
	}

	for _, tc := range testCases {
		r := detectCycle(tc.head)
		if r == nil {
			if tc.want != nil {
				t.Errorf("not nil %v", tc.head)
				continue
			}
		} else {
			if tc.want == nil {
				t.Errorf("nil %v", tc.head)
				continue
			}
			if tc.want.Val != r.Val {
				t.Errorf("not identified %d, %d", tc.want.Val, r.Val)
			}
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
