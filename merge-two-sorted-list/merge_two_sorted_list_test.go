package mergeTwo

import (
	"testing"
)

func TestMergeTwoLists(t *testing.T) {
	testCases := []struct {
		l1     *ListNode
		l2     *ListNode
		expect *ListNode
	}{
		{
			l1: &ListNode{Val: 1, Next: &ListNode{Val: 2, Next: &ListNode{Val: 4, Next: nil}}},
			l2: &ListNode{Val: 1, Next: &ListNode{Val: 3, Next: &ListNode{Val: 4, Next: nil}}},
			expect: &ListNode{
				Val: 1, Next: &ListNode{
					Val: 1, Next: &ListNode{
						Val: 2, Next: &ListNode{
							Val: 3, Next: &ListNode{
								Val: 4, Next: &ListNode{
									Val: 4, Next: nil,
								},
							},
						},
					},
				},
			},
		},
		{
			l1:     nil,
			l2:     nil,
			expect: nil,
		},
		{
			l1: nil,
			l2: &ListNode{Val: 0, Next: nil},
			expect: &ListNode{
				Val: 0, Next: nil,
			},
		},
	}

	for idx, testCase := range testCases {
		res := mergeTwoLists(testCase.l1, testCase.l2)

		if !compareNodes(res, testCase.expect) {
			t.Errorf("%d failed", idx)
		}
	}
}

func compareNodes(n1 *ListNode, n2 *ListNode) bool {
	for {
		if n1 == nil && n2 == nil {
			return true
		}
		if n1 == nil || n2 == nil {
			return false
		}
		if n1.Val != n2.Val {
			return false
		}
		n1 = n1.Next
		n2 = n2.Next
	}
}
