class BrowserHistory:

    def __init__(self, homepage: str):
        self.array = [homepage]
        self.idx = 0

    def visit(self, url: str) -> None:
        self.array = self.array[:self.idx+1]
        self.array.append(url)
        self.idx += 1

    def back(self, steps: int) -> str:
        history = self.idx
        if history < steps:
            self.idx = 0
        else:
            self.idx -= steps

        return self.array[self.idx]

    def forward(self, steps: int) -> str:
        future = len(self.array) - (self.idx+1)
        if future < steps:
            self.idx = len(self.array)-1
        else:
            self.idx += steps

        return self.array[self.idx]        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
