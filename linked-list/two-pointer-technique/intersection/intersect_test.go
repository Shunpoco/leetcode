package intersect

import "testing"

func TestGetIntersectionNode(t *testing.T) {
	intersect1 := &ListNode{8, &ListNode{4, &ListNode{5, nil}}}
	intersect2 := &ListNode{2, &ListNode{4, nil}}
	var testCases = []struct {
		headA *ListNode
		headB *ListNode
		want  *ListNode
	}{
		{
			headA: &ListNode{4, &ListNode{1, intersect1}},
			headB: &ListNode{5, &ListNode{6, &ListNode{1, intersect1}}},
			want:  intersect1,
		},
		{
			headA: &ListNode{1, &ListNode{9, &ListNode{1, intersect2}}},
			headB: &ListNode{3, intersect2},
			want:  intersect2,
		},
		{
			headA: &ListNode{2, &ListNode{6, &ListNode{4, nil}}},
			headB: &ListNode{1, &ListNode{5, nil}},
			want:  nil,
		},
	}

	for _, tc := range testCases {
		if r := getIntersectionNode(tc.headA, tc.headB); r != tc.want {
			t.Errorf("getIntersectionNode(%v, %v) = %v, expected %v", tc.headA, tc.headB, r, tc.want)
		}
	}
}
