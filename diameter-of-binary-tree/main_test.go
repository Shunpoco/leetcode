package main

import "testing"

type test struct {
	root  *TreeNode
	ideal int
}

func TestDiameterOfBinaryTree(t *testing.T) {
	tests := []test{
		{
			&TreeNode{1, &TreeNode{2, &TreeNode{4, nil, nil}, &TreeNode{5, nil, nil}}, &TreeNode{3, nil, nil}},
			3,
		},
	}

	for i, test := range tests {
		actual := diameterOfBinaryTree(test.root)
		if actual != test.ideal {
			t.Errorf("%d\n", i)
		}
	}
}
