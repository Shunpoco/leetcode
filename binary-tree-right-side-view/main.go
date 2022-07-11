package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Item struct {
	Node  *TreeNode
	Level int
}

func rightSideView(root *TreeNode) []int {
	queue := []Item{}
	queue = append(queue, Item{root, 1})
	result := []int{}

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		if v.Node == nil {
			continue
		}

		if len(result) < v.Level {
			result = append(result, v.Node.Val)
		}

		if v.Node.Right != nil {
			queue = append(queue, Item{v.Node.Right, v.Level + 1})
		}
		if v.Node.Left != nil {
			queue = append(queue, Item{v.Node.Left, v.Level + 1})
		}
	}

	return result
}
