package minBt

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type qn struct {
	node  *TreeNode
	depth int
}

func minDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}

	queue := make([]qn, 0, 1024)

	queue = append(queue, qn{root, 1})

	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		if node.node.Left == nil && node.node.Right == nil {
			return node.depth
		}

		if node.node.Left != nil {
			queue = append(queue, qn{node.node.Left, node.depth + 1})
		}

		if node.node.Right != nil {
			queue = append(queue, qn{node.node.Right, node.depth + 1})
		}
	}

	return 0
}
