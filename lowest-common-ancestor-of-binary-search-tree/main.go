package main

// Definition for a binary tree node.
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
	if root.Val == p.Val {
		return p
	}
	if root.Val == q.Val {
		return q
	}
	if p.Val < root.Val && q.Val > root.Val || p.Val > root.Val && q.Val < root.Val {
		return root
	}

	var n *TreeNode

	if p.Val < root.Val {
		n = root.Left
	} else {
		n = root.Right
	}

	return lowestCommonAncestor(n, p, q)
}
