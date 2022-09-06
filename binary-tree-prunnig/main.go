package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func pruneTree(root *TreeNode) *TreeNode {
    return solve(root)
}

func solve(node *TreeNode) *TreeNode {
    if node == nil {
        return nil
    }
    
    contain1 := false
    
    if node.Val == 1 {
        contain1 = true
    }
    
    node.Left = solve(node.Left)
    if node.Left != nil {
        contain1 = true
    }
    
    node.Right = solve(node.Right)
    if node.Right != nil {
        contain1 = true
    }
    
    if contain1 {
        return node
    }
    
    return nil
}
