package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func buildTree(preorder []int, inorder []int) *TreeNode {
	n := len(preorder)

	if n == 1 {
		return &TreeNode{preorder[0], nil, nil}
	} else if n == 0 {
		return nil
	}

	root := preorder[0]

	i := 0
	for inorder[i] != root {
		i++
	}

	in_left := inorder[:i]
	in_right := inorder[i+1:]

	pre_left := preorder[1 : len(in_left)+1]
	pre_right := preorder[len(in_left)+1:]

	return &TreeNode{
		root,
		buildTree(pre_left, in_left),
		buildTree(pre_right, in_right),
	}
}
