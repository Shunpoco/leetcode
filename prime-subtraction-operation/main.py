class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        soe = self.sieve_of_eratosthenes(1000)

        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                continue

            for j in range(2, len(soe)):
                if j >= nums[i]:
                    break

                if not soe[j]:
                    continue

                if nums[i] - j < nums[i+1]:
                    nums[i] -= j
                    break

            if nums[i] >= nums[i+1]:
                return False

        print(nums)
        return True        

    def sieve_of_eratosthenes(self, n: int) -> List[int]:
        result = [True for _ in range(n+1)]
        result[0] = False
        result[1] = False

        i = 2

        while i * i <= n:
            if not result[i]:
                i += 1
                continue
            
            t = i + i
            while t <= n:
                result[t] = False
                t += i

            i += 1

        return result

