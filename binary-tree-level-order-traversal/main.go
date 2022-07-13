package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Tuple struct {
	Node  *TreeNode
	Level int
}

func levelOrder(root *TreeNode) [][]int {
	result := [][]int{}

	if root == nil {
		return result
	}

	queue := []Tuple{{root, 0}}

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		if len(result) == v.Level {
			result = append(result, []int{v.Node.Val})
		} else {
			result[v.Level] = append(result[v.Level], v.Node.Val)
		}

		if v.Node.Left != nil {
			queue = append(queue, Tuple{v.Node.Left, v.Level + 1})
		}

		if v.Node.Right != nil {
			queue = append(queue, Tuple{v.Node.Right, v.Level + 1})
		}
	}

	return result
}
