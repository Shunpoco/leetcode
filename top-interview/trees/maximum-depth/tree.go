package tree

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func maxDepth(root *TreeNode) int {
	max := depth(root, 0)
	return max
}

func depth(node *TreeNode, length int) int {
	if node == nil {
		return length
	}

	ll := depth(node.Left, length+1)
	rl := depth(node.Right, length+1)

	if ll > rl {
		return ll
	}
	return rl
}
