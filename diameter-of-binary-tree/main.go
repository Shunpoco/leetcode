package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func diameterOfBinaryTree(root *TreeNode) int {
	_, result := oneWayAndDiameter(root)

	return result
}

func oneWayAndDiameter(node *TreeNode) (one int, diameter int) {
	if node == nil {
		return
	}

	var left int
	var leftd int
	var right int
	var rightd int

	if node.Left != nil {
		left, leftd = oneWayAndDiameter(node.Left)
		left++
	}

	if node.Right != nil {
		right, rightd = oneWayAndDiameter(node.Right)
		right++
	}

	one = left
	if right > one {
		one = right
	}

	diameter = left + right
	if leftd > diameter {
		diameter = leftd
	}
	if rightd > diameter {
		diameter = rightd
	}

	return
}
