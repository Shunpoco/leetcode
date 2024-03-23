# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head.next is None:
            return
        nodeList = []
        node = head
        while node is not None:
            nodeList.append(node)
            node = node.next

        l = len(nodeList)

        mid: ListNode = None
        if l % 2 != 0:
            mid = nodeList.pop(int(l/2))
            mid.next = None

        pres = nodeList[:int(l/2)]
        posts = nodeList[int(l/2):]
        previous: ListNode = None
        for pre, post in zip(pres, reversed(posts)):
            if previous is not None:
                previous.next = pre

            pre.next = post
            post.next = None
            previous = post

        if mid is not None:
            previous.next = mid
        
