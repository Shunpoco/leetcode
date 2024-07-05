# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        count = 0
        cp = []
        result = [float('inf')]
        prev = None

        while head.next is not None:
            if prev is not None:
                nex = head.next

                if head.val > prev.val and head.val > nex.val or head.val < prev.val and head.val < nex.val:
                    cp.append(count)

                    if len(cp) >= 2 and cp[-1]-cp[-2] < result[0]:
                        result[0] = cp[-1]-cp[-2]

            count += 1
            prev = head
            head = head.next

        if len(cp) < 2:
            return [-1, -1]

        result.append(cp[-1]-cp[0])

        return result

        
