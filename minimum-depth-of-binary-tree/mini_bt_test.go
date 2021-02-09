package minBt

import "testing"

func TestMinDepth(t *testing.T) {
	var testCases = []struct {
		root *TreeNode
		want int
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
			want: 2,
		},
		{
			root: &TreeNode{
				Val:  2,
				Left: nil,
				Right: &TreeNode{
					Val:  3,
					Left: nil,
					Right: &TreeNode{
						Val:  4,
						Left: nil,
						Right: &TreeNode{
							Val:   5,
							Left:  nil,
							Right: leafNode(6),
						},
					},
				},
			},
			want: 5,
		},
	}

	for _, testCase := range testCases {
		if r := minDepth(testCase.root); r != testCase.want {
			t.Errorf("minDepth(%v) = %d, expected %d", testCase.root, r, testCase.want)
		}
	}
}

func leafNode(val int) *TreeNode {
	return &TreeNode{val, nil, nil}
}
