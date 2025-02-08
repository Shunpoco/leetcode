class NumberContainers:
    def __init__(self):
        self.idx_to_num = defaultdict(int)
        self.num_to_idx = {}

    def change(self, index: int, number: int) -> None:
        self.idx_to_num[index] = number

        if self.num_to_idx.get(number) is None:
            self.num_to_idx[number] = []

        heapq.heappush(self.num_to_idx[number], index)        

    def find(self, number: int) -> int:
        if self.num_to_idx.get(number) is None or len(self.num_to_idx[number]) == 0:
            return -1

        v = self.num_to_idx[number][0]
        while self.idx_to_num[v] != number:
            heapq.heappop(self.num_to_idx[number])
            if len(self.num_to_idx[number]) == 0:
                return -1

            v = self.num_to_idx[number][0]

        return v

# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
