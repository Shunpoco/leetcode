package main

/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func getIntersectionNode(headA, headB *ListNode) *ListNode {
    l := [](*ListNode){}
    cur := headA
    for cur != nil {
        l = append(l, cur)
        cur = (*cur).Next
    }
    
    cur = headB
    for cur != nil {
        for _, n := range l {
            if cur == n {
                return cur
            }
        }
        
        cur = (*cur).Next
    }
    
    return nil
}
