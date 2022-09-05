package main

type Node struct {
	Val      int
	Children []*Node
}

type NodeLevel struct {
	Node  *Node
	Level int
}

func levelOrder(root *Node) [][]int {
	result := [][]int{}
	if root == nil {
		return result
	}
	queue := []NodeLevel{{root, 1}}

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		l := len(result)
		if v.Level > l {
			result = append(result, []int{v.Node.Val})
		} else {
			result[l-1] = append(result[l-1], v.Node.Val)
		}

		for _, child := range v.Node.Children {
			queue = append(queue, NodeLevel{child, v.Level + 1})
		}
	}

	return result
}
