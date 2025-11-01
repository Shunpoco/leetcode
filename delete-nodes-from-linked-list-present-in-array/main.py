# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums.sort()

        root = ListNode(val=0, next=head)

        cur = head
        prev = root
        while cur:
            if self.find(cur.val, nums, 0, len(nums)):
                prev.next = cur.next
            else:
                prev = cur
            cur = cur.next

        return root.next


    def find(self, n, nums, left, right):
        if left == right:
            return False

        m = (left+right) // 2

        if nums[m] == n:
            return True

        elif nums[m] > n:
            return self.find(n, nums, left, m)

        return self.find(n, nums, m+1, right)
