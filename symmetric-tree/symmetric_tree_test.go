package symmetricTree

import "testing"

func TestSymmetricTree(t *testing.T) {
	testCases := []struct {
		root     *TreeNode
		expected bool
	}{
		{
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:  3,
						Left: nil,
					},
					Right: &TreeNode{
						Val:   4,
						Right: nil,
					},
				},
				Right: &TreeNode{
					Val: 2,
					Left: &TreeNode{
						Val:  4,
						Left: nil,
					},
					Right: &TreeNode{
						Val:   3,
						Right: nil,
					},
				},
			},
			expected: true,
		},
		{
			root: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:  2,
					Left: nil,
					Right: &TreeNode{
						Val:   3,
						Right: nil,
					},
				},
				Right: &TreeNode{
					Val:  2,
					Left: nil,
					Right: &TreeNode{
						Val:   3,
						Right: nil,
					},
				},
			},
			expected: false,
		},
	}

	for idx, testCase := range testCases {
		if isSymmetric(testCase.root) != testCase.expected {
			t.Errorf("%d", idx)
		}
	}
}
