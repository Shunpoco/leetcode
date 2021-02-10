package pathSum

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func hasPathSum(root *TreeNode, targetSum int) bool {
	return hasPath(root, targetSum)
}

func hasPath(node *TreeNode, sum int) bool {
	if node == nil {
		return false
	}

	if isLeafNode(node) {
		if sum-node.Val == 0 {
			return true
		}
		return false
	}

	nextSum := sum - node.Val

	resL := hasPath(node.Left, nextSum)
	if resL {
		return true
	}
	resR := hasPath(node.Right, nextSum)
	if resR {
		return true
	}

	return false
}

func isLeafNode(node *TreeNode) bool {
	if node == nil {
		return false
	}
	if node.Left == nil && node.Right == nil {
		return true
	}

	return false
}
