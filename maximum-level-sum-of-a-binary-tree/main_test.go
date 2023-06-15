package main

import "testing"

type test struct {
	name  string
	input []int
	want  int
}

const null = -1000000

func TestMaxLevelSum(t *testing.T) {
	tests := []test{
		{
			name:  "1",
			input: []int{1, 7, 0, -8, null, null},
			want:  2,
		},
		{
			name:  "2",
			input: []int{989, null, 10250, 98693, -89388, null, null, null, -32127},
			want:  2,
		},
		{
			name:  "3",
			input: []int{1},
			want:  1,
		},
		{
			name:  "4",
			input: []int{-100, -200, -300, -20, -5, -10, null},
			want:  3,
		},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			root := makeTreeHelper(tt.input)
			if got := maxLevelSum(root); got != tt.want {
				t.Errorf("%d != %d\n", got, tt.want)
			}
		})
	}
}

func makeTreeHelper(input []int) *TreeNode {
	root := &TreeNode{
		Val:   input[0],
		Left:  nil,
		Right: nil,
	}

	input = input[1:]
	queue := make([]*TreeNode, 0, 10000)
	queue = append(queue, root)
	for len(queue) > 0 {
		node := queue[0]
		queue = queue[1:]

		if len(input) > 0 {
			if input[0] != null {
				l := &TreeNode{
					Val:   input[0],
					Left:  nil,
					Right: nil,
				}
				node.Left = l
				queue = append(queue, l)

			}
			input = input[1:]
		}

		if len(input) > 0 {
			if input[0] != null {
				r := &TreeNode{
					Val:   input[0],
					Left:  nil,
					Right: nil,
				}
				node.Right = r
				queue = append(queue, r)
			}
			input = input[1:]
		}
	}

	return root
}
