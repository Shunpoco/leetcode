class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefixes = [0 for _ in range(len(nums))]
        prefixes[0] = nums[0]

        for i in range(1, len(nums)):
            prefixes[i] = prefixes[i-1] ^ nums[i]

        result = [0 for _ in range(len(nums))]

        mask = (1 << maximumBit) - 1

        for i in range(len(nums)):
            cur = prefixes[len(prefixes)-1-i]
            result[i] = cur ^ mask

        return result

