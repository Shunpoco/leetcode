package pathSum

import "testing"

func TestHasPathSum(t *testing.T) {
	var testCases = []struct {
		root      *TreeNode
		targetSum int
		want      bool
	}{
		{
			root: &TreeNode{
				Val: 5,
				Left: &TreeNode{
					Val: 4,
					Left: &TreeNode{
						Val:   11,
						Left:  leafNode(7),
						Right: leafNode(2),
					},
					Right: nil,
				},
				Right: &TreeNode{
					Val:  8,
					Left: leafNode(13),
					Right: &TreeNode{
						Val:   4,
						Left:  nil,
						Right: leafNode(1),
					},
				},
			},
			targetSum: 22,
			want:      true,
		},
		{
			root: &TreeNode{
				Val:   1,
				Left:  leafNode(2),
				Right: leafNode(3),
			},
			targetSum: 5,
			want:      false,
		},
		{
			root:      nil,
			targetSum: 0,
			want:      false,
		},
	}

	for _, testCase := range testCases {
		if r := hasPathSum(testCase.root, testCase.targetSum); r != testCase.want {
			t.Errorf("hasPathSum(%v, %d) == %v, expected %v", testCase.root, testCase.targetSum, r, testCase.want)
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
