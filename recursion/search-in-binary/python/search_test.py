# Under construction

from typing import List
import unittest

from search import Solution, TreeNode

class TestSearchBST(unittest.TestCase):
    def setUp(self):
        self.s = Solution()

        self.testCases = [
            {
                'root': [4,2,7,1,3],
                'val': 2,
                'want': [2,1,3],
            },
            {
                'root': [4,2,5,1,3],
                'val': 5,
                'want': [],
            },
            {
                'want': [4,2,7,-1,3, 5],
                'val': 2,
                'want': [2, -1, 3],
            },
        ]

    def numsToTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None

        head = TreeNode(nums[0])
        parents = [head]
        current = parents.pop(0)
        c = 0
        for i in range(1, len(nums)):
            v = nums[i]
            if v > 0:
                node = TreeNode(nums[i])
            if current.left == None:
                current.left = node
            else:
                current.right = node
            parents.append(node)
            c += 1
            if c == 2:
                current = parents.pop(0)
                c = 0

        return head

    def treeToNums(self, head: TreeNode, layer: int) -> List[int]:
        nums = []

        search = [head]
        c = 0
        cur = None
        i = 0
        while i < layer:
            cur = search.pop(0)

            if cur.

            l = cur.left
            if l is not None:
                nums.append(l.val)

            r = cur.right
            if r is not None:
                nums.append(r.val)
