from collections import defaultdict
import bisect

class SummaryRanges:

    def __init__(self):
        self.nums = [-1 for _ in range(10001)]
        self.intervals = defaultdict(int)

    def addNum(self, value: int) -> None:
        if self.nums[value] >= 0:
            return
        
        if value > 0 and self.nums[value-1] >= 0:
            parent = self.nums[value-1]
            self.nums[value] = parent
            self.intervals[parent] = value
        else:
            self.intervals[value] = value
            self.nums[value] = value

        if value < 10000 and self.nums[value+1] >= 0:
            child = self.nums[value+1]
            parent = self.nums[value]
            self.nums[child] = parent
            grandchild = self.intervals.pop(child)
            self.nums[grandchild] = parent
            self.intervals[parent] = grandchild


    def getIntervals(self) -> List[List[int]]:
        r = []
        for start, end in self.intervals.items():
            bisect.insort(r, [start, end])

        return r

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()
