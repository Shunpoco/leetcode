class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()

        mb = items[0][1]

        for i in range(len(items)):
            mb = max(mb, items[i][1])
            items[i][1] = mb

        return [self.search(items, q) for q in queries]

    def search(self, items, target):
        left = 0
        right = len(items)-1

        mb = 0

        while left <= right:
            m = (left+right) // 2

            if items[m][0] > target:
                right = m-1

            else:
                mb = max(mb, items[m][1])
                left = m + 1

        return mb

