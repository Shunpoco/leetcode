from typing import List


class UnionFind:
    def __init__(self, val: int):
        self.v = val
        self.p = None
        self.l = 1

    def parent(self) -> "UnionFind":
        if self.p is None:
            return self

        else:
            return self.p.parent()

    def union(self, child: "UnionFind"):
        root = child.parent()

        root.p = self
        self.l += root.l
        root.l = self.l



class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        memory = {}

        for num in nums:
            if memory.get(num) is not None:
                continue
            n = UnionFind(num)
            if memory.get(num+1) is not None:
                n.union(memory[num+1])

            if memory.get(num-1) is not None:
                memory[num-1].union(n)

            memory[num] = n

        result = 0
        for _, uf in memory.items():
            if uf.l > result:
                result = uf.l

        return result
