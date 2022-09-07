package main

import (
	"fmt"
	"strconv"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func tree2str(root *TreeNode) string {
	return solve(root)
}

func solve(node *TreeNode) string {
	if node == nil {
		return ""
	}

	result := strconv.Itoa(node.Val)

	left := ""
	if node.Left != nil {
		left = solve(node.Left)
	}

	right := ""
	if node.Right != nil {
		right = solve(node.Right)
	}

	if right != "" {
		left = fmt.Sprintf("(%s)", left)
		right = fmt.Sprintf("(%s)", right)

		result = fmt.Sprintf("%s%s%s", result, left, right)
	} else if left != "" {
		left = fmt.Sprintf("(%s)", left)
		result = fmt.Sprintf("%s%s", result, left)
	}

	return result
}
