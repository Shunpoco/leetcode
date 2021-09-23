package invert

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func invertTree(root *TreeNode) *TreeNode {
	if root == nil || isLeaf(root) {
		return root
	}

	left := invertTree(root.Left)
	right := invertTree(root.Right)

	root.Left = right
	root.Right = left

	return root
}

func isLeaf(node *TreeNode) bool {
	if node.Left == nil && node.Right == nil {
		return true
	}
	return false
}
