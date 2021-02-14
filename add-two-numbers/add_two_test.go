package add_two

import (
	"reflect"
	"testing"
)

func TestAddTwoNumbers(t *testing.T) {
	var testCases = []struct {
		l1   *ListNode
		l2   *ListNode
		want *ListNode
	}{
		{
			l1:   &ListNode{2, &ListNode{4, &ListNode{3, nil}}},
			l2:   &ListNode{5, &ListNode{6, &ListNode{4, nil}}},
			want: &ListNode{7, &ListNode{0, &ListNode{8, nil}}},
		},
		{
			l1:   &ListNode{0, nil},
			l2:   &ListNode{0, nil},
			want: &ListNode{0, nil},
		},
		{
			l1:   &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, nil}}}}}}},
			l2:   &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{9, nil}}}},
			want: &ListNode{8, &ListNode{9, &ListNode{9, &ListNode{9, &ListNode{0, &ListNode{0, &ListNode{0, &ListNode{1, nil}}}}}}}},
		},
	}

	for _, tc := range testCases {
		if r := addTwoNumbers(tc.l1, tc.l2); !reflect.DeepEqual(r, tc.want) {
			t.Errorf("addTwoNumbers(%v, %v) == %v, expected %v", tc.l1, tc.l2, r, tc.want)
		}
	}
}
