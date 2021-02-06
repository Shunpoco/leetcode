package bt

import (
	"reflect"
	"testing"
)

func TestLevelOrderBottom(t *testing.T) {
	var testCases = []struct {
		root *TreeNode
		want [][]int
	}{
		{
			root: &TreeNode{
				Val:  3,
				Left: leafNode(9),
				Right: &TreeNode{
					Val:   20,
					Left:  leafNode(15),
					Right: leafNode(7),
				},
			},
			want: [][]int{
				[]int{15, 7},
				[]int{9, 20},
				[]int{3},
			},
		},
		{root: nil, want: [][]int{}},
	}

	for _, testCase := range testCases {
		if r := levelOrderBottom(testCase.root); !reflect.DeepEqual(r, testCase.want) {
			t.Errorf("levelOrderBottom(%v) = %v, expected %v", testCase.root, r, testCase.want)
		}
	}
}

func leafNode(val int) *TreeNode {
	return &TreeNode{
		Val:   val,
		Left:  nil,
		Right: nil,
	}
}
