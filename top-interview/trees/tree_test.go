package tree

import "testing"

func TestMaxDepth(t *testing.T) {
	var testCases = []struct {
		root *TreeNode
		want int
	}{
		{
			&TreeNode{3, leafNode(9), &TreeNode{20, leafNode(15), leafNode(7)}},
			3,
		},
		{
			&TreeNode{1, nil, leafNode(2)},
			2,
		},
		{
			nil,
			0,
		},
		{
			&TreeNode{0, nil, nil},
			1,
		},
	}

	for _, tc := range testCases {
		if r := maxDepth(tc.root); r != tc.want {
			t.Errorf("maxDepth(%v) = %d, expected %d", tc.root, r, tc.want)
		}
	}
}

func leafNode(val int) *TreeNode {
	return &TreeNode{val, nil, nil}
}
