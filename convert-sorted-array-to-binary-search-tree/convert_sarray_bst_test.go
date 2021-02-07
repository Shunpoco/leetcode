package convert

import (
	"reflect"
	"testing"
)

func TestSortedArrayToBST(t *testing.T) {
	var testCases = []struct {
		nums []int
		want *TreeNode
	}{
		{
			nums: []int{-10, -3, 0, 5, 9},
			want: &TreeNode{
				Val: 0,
				Left: &TreeNode{
					Val:   -3,
					Left:  leafNode(-10),
					Right: nil,
				},
				Right: &TreeNode{
					Val:   9,
					Left:  leafNode(5),
					Right: nil,
				},
			},
		},
	}

	for _, testCase := range testCases {
		if r := sortedArrayToBST(testCase.nums); !reflect.DeepEqual(r, testCase.want) {
			t.Errorf("sortedArrayToBST(%v) = %v, not %v", testCase.nums, r, testCase.want)
		}
	}
}

func leafNode(num int) *TreeNode {
	return &TreeNode{num, nil, nil}
}
