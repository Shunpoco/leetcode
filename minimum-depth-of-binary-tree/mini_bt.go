package minBt

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	return depth(root, 0)
}

func depth(node *TreeNode, start int) int {
	if node == nil {
		return 1000000
	}

	if isLeafNode(node) {
		return start + 1
	}

	dL := depth(node.Left, start+1)
	dR := depth(node.Right, start+1)

	if dL >= dR {
		return dR
	}
	return dL
}

func isLeafNode(node *TreeNode) bool {
	if node.Right == nil && node.Left == nil {
		return true
	}

	return false
}
