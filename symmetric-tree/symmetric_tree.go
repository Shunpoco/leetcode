package symmetricTree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isSymmetric(root *TreeNode) bool {
	if root == nil {
		return true
	}
	return isSymmetricTwoTree(root.Left, root.Right)
}

func isSymmetricTwoTree(p *TreeNode, q *TreeNode) bool {
	if p == nil && q == nil {
		return true
	}

	if p == nil || q == nil || p.Val != q.Val {
		return false
	}

	return isSymmetricTwoTree(p.Left, q.Right) && isSymmetricTwoTree(p.Right, q.Left)
}
