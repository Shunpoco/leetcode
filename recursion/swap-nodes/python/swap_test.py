from typing import List
import unittest

from swap import ListNode, Solution

class TestSwapPairs(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'head': [1,2,3,4],
                'want': [2,1,4,3],
            },
            {
                'head': [],
                'want': [],
            },
            {
                'head': [1],
                'want': [1],
            },
        ]

    def numsToListNode(self, nums: List[int]) -> ListNode:
        if len(nums) == 0:
            return None
        head = ListNode(nums[0], None)
        current = head
        for i in range(1, len(nums)):
            node = ListNode(nums[i], None)
            current.next = node
            current = node

        return head

    def listNodeToNums(self, head: ListNode) -> List[int]:
        nums = []

        while head is not None:
            nums.append(head.val)
            head = head.next

        return nums

    def test(self):
        for tc in self.testCases:
            with self.subTest(tc=tc):
                head = self.numsToListNode(tc['head'])
                swapped = self.s.swapPairs(head)
                self.assertEqual(
                    self.listNodeToNums(swapped),
                    tc['want'],
                )

if __name__ == '__main__':
    unittest.main()
