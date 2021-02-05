package mdbt

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	lM := maxDepth(root.Left)
	rM := maxDepth(root.Right)

	if lM >= rM {
		return lM + 1
	}
	return rM + 1
}
