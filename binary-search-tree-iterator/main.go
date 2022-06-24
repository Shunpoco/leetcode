package main

/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type Heap []int

func (h Heap) Len() int {
    return len(h)
}

func (h *Heap) Swap(i, j int) {
    (*h)[i], (*h)[j] = (*h)[j], (*h)[i]
}

func (h *Heap) Push(nums int) {
    n := (*h).Len()
    *h = append(*h, nums)
    
    var p int
    if n%2 == 0 {
        p = (n-2)/2
    } else {
        p = (n-1)/2
    }
    
    for p >= 0 && (*h)[p] > (*h)[n] {
        h.Swap(p, n)
        n = p
        if n%2 == 0 {
            p = (n-2)/2
        } else {
            p = (n-1)/2
        }
    }
}

func (h *Heap) Pop() int {
    n := (*h).Len()
    result := (*h)[0]
    (*h)[0] = (*h)[n-1]
    *h = (*h)[:n-1]
    
    base := 0
    idx := 0
    left := 2*base+1
    right := 2*base+2
    for left < n-1 {
        if (*h)[idx] > (*h)[left] {
            idx = left
        }
        
        if right < n-1 && (*h)[idx] > (*h)[right] {
            idx = right
        }
        
        if idx == base {
            break;
        }
        
        h.Swap(base, idx)
        base = idx
        left = 2*base+1
        right = 2*base+2
    }
    
    return result
}

type BSTIterator struct {
    heap *Heap
}


func Constructor(root *TreeNode) BSTIterator {
    h := Heap{}
    stack := []*TreeNode{root}
    for len(stack) > 0 {
        node := stack[len(stack)-1]
        stack = stack[:len(stack)-1]
        h.Push(node.Val)
        if node.Left != nil {
            stack = append(stack, node.Left)
        }
        if node.Right != nil {
            stack = append(stack, node.Right)
        }
    }
    return BSTIterator{&h}
}


func (this *BSTIterator) Next() int {
    return this.heap.Pop()
}


func (this *BSTIterator) HasNext() bool {
    return this.heap.Len() > 0
}


/**
 * Your BSTIterator object will be instantiated and called as such:
 * obj := Constructor(root);
 * param_1 := obj.Next();
 * param_2 := obj.HasNext();
 */
