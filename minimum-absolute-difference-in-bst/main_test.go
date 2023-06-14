package main

import (
	"testing"
)

type test struct {
	bst   []int
	ideal int
}

func TestGetMinimumDifference(t *testing.T) {
	tests := []test{
		{
			[]int{4, 2, 6, 1, 3},
			1,
		},
		{
			[]int{1, 0, 48, -1, -1, 12, 49},
			1,
		},
	}

	for i, test := range tests {
		tree := makeTree(test.bst)
		if actual := getMinimumDifference(tree); actual != test.ideal {
			t.Errorf("Case %d: getMinimumDifference(%v) = %d should match %d\n", i, test.bst, actual, test.ideal)
		}
	}
}

func makeTree(bst []int) *TreeNode {
	queue := make([]*TreeNode, 0, len(bst))

	root := &TreeNode{bst[0], nil, nil}
	queue = append(queue, root)
	bst = bst[1:]
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]
		// left
		if len(bst) > 0 {
			if bst[0] >= 0 {
				left := &TreeNode{bst[0], nil, nil}
				node.Left = left
				queue = append(queue, left)
			}
			bst = bst[1:]
		}

		if len(bst) > 0 {
			if bst[0] >= 0 {
				right := &TreeNode{bst[0], nil, nil}
				node.Right = right
				queue = append(queue, right)
			}
			bst = bst[1:]
		}
	}

	return root
}
