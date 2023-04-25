from collections import heapq

class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.cur = 1
        

    def popSmallest(self) -> int:
        v = self.cur
        if len(self.heap) > 0:
            v = heapq.heappop(self.heap)
            while len(self.heap) > 0 and self.heap[0] == v:
                heapq.heappop(self.heap)
        else:
            self.cur += 1
        
        return v
        

    def addBack(self, num: int) -> None:
        if num < self.cur:
            heapq.heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
