class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        # the odd index has odd value and even index has even value
        # or odd index has even value and even index has odd value
        # or all index has odd
        # or all index had even

        first_odd = -1
        first_even = -1
        for i, v in enumerate(nums):
            if v % 2 != 0:
                first_odd = i
                break
        for i, v in enumerate(nums):
            if v % 2 == 0:
                first_even = i
                break

        result = 0

        # odd + even or even + odd
        if first_odd > -1 and first_even > -1:
            t = 1
            nex = 0
            for i in range(first_odd+1, len(nums)):
                if nums[i] % 2 == nex:
                    nex ^= 1
                    t += 1
            if t > result:
                result = t

            t = 1
            nex = 1
            for i in range(first_even+1, len(nums)):
                if nums[i] % 2 == nex:
                    nex ^= 1
                    t += 1

            if t > result:
                result = t

        # Only odd
        if first_odd > -1:
            t = 1
            for i in range(first_odd+1, len(nums)):
                if nums[i] % 2 != 0:
                    t += 1

            if t > result:
                result = t

        # Only even
        if first_even > -1:
            t = 1
            for i in range(first_even+1, len(nums)):
                if nums[i] % 2 == 0:
                    t += 1

            if t > result:
                result = t

        return result

