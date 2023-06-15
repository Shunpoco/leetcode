package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

type Var struct {
	Node  *TreeNode
	Level int
}

func maxLevelSum(root *TreeNode) int {
	results := make([]int, 0, 16)

	queue := make([]Var, 0, 10000)
	queue = append(queue, Var{root, 1})

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		if len(results) < v.Level {
			results = append(results, v.Node.Val)
		} else {
			results[v.Level-1] += v.Node.Val
		}

		if v.Node.Left != nil {
			queue = append(queue, Var{v.Node.Left, v.Level + 1})
		}

		if v.Node.Right != nil {
			queue = append(queue, Var{v.Node.Right, v.Level + 1})
		}
	}

	result := 1
	s := results[0]
	for l, v := range results {
		if s < v {
			s = v
			result = l + 1
		}
	}

	return result
}
