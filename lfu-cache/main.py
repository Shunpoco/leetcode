from collections import defaultdict

class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.total = 0
        self.cache = defaultdict(tuple)
        self.log = defaultdict(list)
        self.minf = 0

    def get(self, key: int) -> int:
        if self.cache.get(key):
            val, cnt = self.cache[key]
            self.cache[key] = (val, cnt+1)
            self.log[cnt+1].append(key)
            i = self.log[cnt].index(key)
            self.log[cnt].pop(i)
            if self.minf == cnt and len(self.log[cnt]) == 0:
                self.minf += 1
            return val
        return -1
        

    def put(self, key: int, value: int) -> None:
        if self.capacity <= 0:
            return
        if self.cache.get(key) is None:
            if self.total == self.capacity:
                v = self.log[self.minf].pop(0)
                self.cache.pop(v)
                self.total -= 1
            self.cache[key] = (value, 1)
            self.log[1].append(key)
            self.total += 1
            self.minf = 1
        else:
            _, cnt = self.cache[key]
            self.cache[key] = (value, cnt+1)
            self.log[cnt+1].append(key)
            i = self.log[cnt].index(key)
            self.log[cnt].pop(i)
            if self.minf == cnt and len(self.log[cnt]) == 0:
                self.minf += 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
