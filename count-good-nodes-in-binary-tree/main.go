package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func goodNodes(root *TreeNode) int {
	return solve(root, -100000)
}

func solve(node *TreeNode, max int) int {
	result := 0

	if node.Val >= max {
		result++
		max = node.Val
	}

	if node.Left != nil {
		result += solve(node.Left, max)
	}

	if node.Right != nil {
		result += solve(node.Right, max)
	}

	return result
}
