package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if p.Val > q.Val {
		return lowestCommonAncestor(root, q, p)
	}

	if p.Val == root.Val || q.Val == root.Val || p.Val < root.Val && q.Val > root.Val {
		return root
	}

	if p.Val > root.Val {
		return lowestCommonAncestor(root.Right, p, q)
	}

	// q.Val < root.Val
	return lowestCommonAncestor(root.Left, p, q)
}
