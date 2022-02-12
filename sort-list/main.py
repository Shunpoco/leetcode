# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.s(head)
        
    def s(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        left_last, right_first = self.middleNode(head)
        left_last.next = None
        left = self.s(head)
        right = self.s(right_first)
        
        return self.mergeTwoLists(left, right)

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [head]
        
        while arr[-1].next:
            arr.append(arr[-1].next)
            
        return arr[len(arr) // 2 - 1], arr[len(arr) // 2]
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0, None)
        cur = head
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
                
            cur = cur.next
            
        while list1:
            cur.next = list1
            list1 = list1.next
            cur = cur.next
            
        while list2:
            cur.next = list2
            list2 = list2.next
            cur = cur.next
            
        return head.next
