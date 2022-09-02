package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type NodeLevel struct {
	Node  *TreeNode
	Level int
}

func averageOfLevels(root *TreeNode) []float64 {
	queue := []NodeLevel{{root, 0}}
	result := []float64{}

	s := 0.0
	c := 0
	l := -1
	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]
		if l == -1 || l == v.Level {
			s += float64(v.Node.Val)
			c++
		} else {
			r := s / float64(c)
			result = append(result, r)
			s = float64(v.Node.Val)
			c = 1
		}
		l = v.Level
		if v.Node.Left != nil {
			queue = append(queue, NodeLevel{v.Node.Left, v.Level + 1})
		}
		if v.Node.Right != nil {
			queue = append(queue, NodeLevel{v.Node.Right, v.Level + 1})
		}
	}

	r := s / float64(c)
	result = append(result, r)

	return result
}
