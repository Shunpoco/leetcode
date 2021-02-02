package sameTree

import "testing"

func TestIsSameTree(t *testing.T) {
	testCases := []struct {
		p        *TreeNode
		q        *TreeNode
		expected bool
	}{
		{
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  nil,
					Right: nil,
				},
				Right: &TreeNode{
					Val:   3,
					Left:  nil,
					Right: nil,
				},
			},
			q: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  nil,
					Right: nil,
				},
				Right: &TreeNode{
					Val:   3,
					Left:  nil,
					Right: nil,
				},
			},
			expected: true,
		},
		{
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  nil,
					Right: nil,
				},
				Right: nil,
			},
			q: &TreeNode{
				Val:  1,
				Left: nil,
				Right: &TreeNode{
					Val:   3,
					Left:  nil,
					Right: nil,
				},
			},
			expected: false,
		},
		{
			p: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   2,
					Left:  nil,
					Right: nil,
				},
				Right: &TreeNode{
					Val:   1,
					Left:  nil,
					Right: nil,
				},
			},
			q: &TreeNode{
				Val: 1,
				Left: &TreeNode{
					Val:   1,
					Left:  nil,
					Right: nil,
				},
				Right: &TreeNode{
					Val:   1,
					Left:  nil,
					Right: nil,
				},
			},
			expected: false,
		},
	}

	for idx, testCase := range testCases {
		if isSameTree(testCase.p, testCase.q) != testCase.expected {
			t.Errorf("%d", idx)
		}
	}
}
