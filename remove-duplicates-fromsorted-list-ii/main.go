package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
import "fmt"

func deleteDuplicates(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    
    root := ListNode{-101, nil}
    pos := &root
    node := head
    prev := &root
    pv := -101
    dup := false
    for node != nil {
        if (*node).Val == pv {
            dup = true
        } else {
            if !dup && *prev != root {
                (*pos).Next = prev
                pos = prev
                prev.Next = nil
            }
            prev = node
            dup = false
        }
        pv = (*node).Val
        node = (*node).Next
    }
    
    if !dup && prev != nil {
        (*pos).Next = prev
    }
    
    return root.Next
}
