class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.memo1 = defaultdict(int)
        self.memo2 = defaultdict(int)

        for num in nums1:
            self.memo1[num] += 1
        for num in nums2:
            self.memo2[num] += 1


    def add(self, index: int, val: int) -> None:
        v = self.nums2[index]
        newv = v + val

        self.memo2[v] -= 1
        self.memo2[newv] += 1
        self.nums2[index] = newv


    def count(self, tot: int) -> int:
        result = 0

        for v, c1 in self.memo1.items():
            t = tot - v
            if t > 0:
                c2 = self.memo2[t]
                result += c1 * c2

        return result

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
