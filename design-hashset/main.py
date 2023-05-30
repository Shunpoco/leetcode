class MyHashSet:

    def __init__(self):
        self._size = 1000
        self.memory = [[] for _ in range(self._size)]
        
    def _hash(self, val: int) -> int:
        return val % self._size

    def add(self, key: int) -> None:
        v = self._hash(key)

        if key not in self.memory[v]:
            self.memory[v].append(key)

    def remove(self, key: int) -> None:
        v = self._hash(key)
        if key in self.memory[v]:
            self.memory[v].remove(key)

    def contains(self, key: int) -> bool:
        v = self._hash(key)

        return key in self.memory[v]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
