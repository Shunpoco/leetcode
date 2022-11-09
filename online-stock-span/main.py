from typing import List, Tuple

class StockSpanner:

    def __init__(self):
        self.mem: List[Tuple[int, int]] = []

    def next(self, price: int) -> int:
        if len(self.mem) == 0 or self.mem[-1][0] > price:
            self.mem.append((price, 1))
            return 1
        
        c = 1
        l = len(self.mem)-1
        pv, pc = self.mem[l]
        while l >= 0:
            pv, pc = self.mem[l]
            if pv > price:
                break
            c += pc
            l -= pc
            
        self.mem.append((price, c))
        
        return c
        

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
