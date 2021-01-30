package removeDup

import (
	"fmt"
	"reflect"
	"testing"
)

func TestDeleteDuplicates(t *testing.T) {
	testCases := []struct {
		head     *ListNode
		expected *ListNode
	}{
		{
			head: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 1,
					Next: &ListNode{
						Val:  2,
						Next: nil,
					},
				},
			},
			expected: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val:  2,
					Next: nil,
				},
			},
		},
		{
			head: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 1,
					Next: &ListNode{
						Val: 2,
						Next: &ListNode{
							Val: 3,
							Next: &ListNode{
								Val:  3,
								Next: nil,
							},
						},
					},
				},
			},
			expected: &ListNode{
				Val: 1,
				Next: &ListNode{
					Val: 2,
					Next: &ListNode{
						Val:  3,
						Next: nil,
					},
				},
			},
		},
		{
			head:     nil,
			expected: nil,
		},
	}

	for idx, testCase := range testCases {
		res := deleteDuplicates(testCase.head)

		if !compare(res, testCase.expected) {
			t.Errorf("%d", idx)
		}
	}
}

func compare(a *ListNode, b *ListNode) bool {

	sA := []int{}
	sB := []int{}

	next := a
	for next != nil {
		sA = append(sA, next.Val)
		next = next.Next
	}

	next = b
	for next != nil {
		if next == nil {
			break
		}
		sB = append(sB, next.Val)
		next = next.Next
	}

	fmt.Println(sA)
	fmt.Println(sB)

	return reflect.DeepEqual(sA, sB)
}
