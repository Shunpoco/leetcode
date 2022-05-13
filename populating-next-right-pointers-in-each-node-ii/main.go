package main

type Node struct {
	Val   int
	Left  *Node
	Right *Node
	Next  *Node
}

type Comb struct {
	Node  *Node
	Level int
}

func connect(root *Node) *Node {
	queue := []*Comb{
		{root, 1},
	}

	for len(queue) > 0 {
		v := queue[0]
		queue = queue[1:]

		if v.Node != nil {
			if len(queue) > 0 && v.Level == queue[0].Level {
				v.Node.Next = queue[0].Node
			}

			if v.Node.Left != nil {
				queue = append(queue, &Comb{v.Node.Left, v.Level + 1})
			}

			if v.Node.Right != nil {
				queue = append(queue, &Comb{v.Node.Right, v.Level + 1})
			}
		}
	}

	return root
}
