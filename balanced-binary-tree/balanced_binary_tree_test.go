package bbt

import "testing"

func TestIsBalanced(t *testing.T) {
	var testCases = []struct {
		root *TreeNode
		want bool
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
			want: true,
		},
		{
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:   3,
						Left:  leafNode(4),
						Right: leafNode(4),
					},
					Right: leafNode(3),
				},
				Right: leafNode(2),
			},
			want: false,
		},
		{
			root: nil,
			want: true,
		},
		{
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:   3,
						Left:  leafNode(4),
						Right: nil,
					},
					Right: nil,
				},
				Right: &TreeNode{
					Val:  2,
					Left: nil,
					Right: &TreeNode{
						Val:   3,
						Left:  nil,
						Right: leafNode(4),
					},
				},
			},
		},
	}

	for _, testCase := range testCases {
		if r := isBalanced(testCase.root); r != testCase.want {
			t.Errorf("isBalanced(%v) = %v, expected %v", testCase.root, r, testCase.want)
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
