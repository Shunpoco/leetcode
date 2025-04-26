class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        sums = sum(nums)

        answer = [-1 for _ in range(len(queries))]

        for i, q in enumerate(queries):
            t = sums
            cur = len(nums)-1

            while t > q and cur >= 0:
                t -= nums[cur]
                cur -= 1

            answer[i] = cur + 1

        return answer
