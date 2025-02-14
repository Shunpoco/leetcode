class ProductOfNumbers:
    def __init__(self):
        self.p = [1]
        self.len = 0

    def add(self, num: int) -> None:
        if num == 0:
            self.p = [1]
            self.len = 0

        else:
            self.p.append(self.p[self.len]*num)
            self.len += 1

    def getProduct(self, k: int) -> int:
        if k > self.len:
            return 0

        return self.p[self.len] // self.p[self.len-k]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
