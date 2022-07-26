package main

type TreeNode struct {
    Val int
    Left *TreeNode
    Right *TreeNode
}
func lowestCommonAncestor(root, p, q *TreeNode) *TreeNode {
    _, result := search(root, p, q)
    
    return result
}

func search(root, p, q *TreeNode) (int, *TreeNode) {
    result := root
    var val int
    if root.Val == p.Val || root.Val == q.Val {
        val++
    }
    
    var t *TreeNode
    if root.Left != nil {
        v, n := search(root.Left, p, q)
        if v == 2 {
            result = n
            val = 2
        } else if v == 1 && val == 1 {
            val = 2
        } else if v == 1 && val == 0 {
            val = 1
            t = n
        }
    }
    
    if root.Right != nil {
        v, n := search(root.Right, p, q)
        if v == 2 {
            result = n
            val = 2
        } else if v == 1 && val == 1 {
            val = 2
        } else if v == 1 && val == 0 {
            val = 1
            t = n
        }
    }
    
    if val == 1 && t != nil {
        result = t
    }
    
    return val, result
}
