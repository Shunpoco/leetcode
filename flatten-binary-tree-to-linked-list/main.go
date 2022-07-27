package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func flatten(root *TreeNode) {
	if root == nil {
		return
	}

	stack := []*TreeNode{root}
	cur := &TreeNode{-1, nil, nil}
	for len(stack) > 0 {
		node := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		cur.Right = node
		if node.Right != nil {
			stack = append(stack, node.Right)
			node.Right = nil
		}
		if node.Left != nil {
			stack = append(stack, node.Left)
			node.Left = nil
		}

		cur = node
	}

	root = cur.Right
}
