package bbt

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	result, _ := treeHeight(root, 0)
	return result
}

func treeHeight(node *TreeNode, height int) (bool, int) {
	if node == nil {
		return true, height
	}

	leftT, leftH := treeHeight(node.Left, height+1)
	rightT, rightH := treeHeight(node.Right, height+1)

	if leftH >= rightH {
		return (leftT && rightT && (leftH-rightH <= 1)), leftH
	}
	return (leftT && rightT && (rightH-leftH <= 1)), rightH
}
