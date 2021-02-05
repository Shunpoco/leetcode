package mdbt

import "testing"

func TestMaxDepth(t *testing.T) {
	var testCases = []struct {
		root     *TreeNode
		expected int
	}{
		{
			&TreeNode{
				Val:  3,
				Left: leafNode(9),
				Right: &TreeNode{
					Val:   20,
					Left:  leafNode(15),
					Right: leafNode(7),
				},
			},
			3,
		},
		{
			&TreeNode{
				Val:   1,
				Left:  nil,
				Right: leafNode(2),
			},
			2,
		},
		{
			nil,
			0,
		},
	}

	for _, testCase := range testCases {
		if r := maxDepth(testCase.root); r != testCase.expected {
			t.Errorf("maxDepth(%v) = %d, not %d", testCase.root, r, testCase.expected)
		}
	}
}

func leafNode(val int) *TreeNode {
	return &TreeNode{val, nil, nil}
}
