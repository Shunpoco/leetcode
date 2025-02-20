class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        def g(cur):
            if len(cur) == n:
                if cur not in nums:
                    return cur
                return ""

            v = g(cur+"0")
            if len(v) == n:
                return v

            return g(cur+"1")

        return g("")
