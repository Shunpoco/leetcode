class MyHashMap:

    def __init__(self):
        self.mod = 1000
        self.hash = [[] for _ in range(self.mod)]

    def put(self, key: int, value: int) -> None:
        m = key % self.mod

        for i, kv in enumerate(self.hash[m]):
            if kv[0] == key:
                self.hash[m][i] = (key, value)
                return
        self.hash[m].append((key, value))

    def get(self, key: int) -> int:
        m = key % self.mod

        cand = self.hash[m]

        for k, value in cand:
            if k == key:
                return value

        return -1 

    def remove(self, key: int) -> None:
        m = key % self.mod

        for i, kv in enumerate(self.hash[m]):
            if kv[0] == key:
                self.hash[m].pop(i)
                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
