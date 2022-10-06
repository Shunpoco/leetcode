from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.d = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.d[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        values = self.d[key]

        if len(values) == 0:
            return ""
        
        left = 0
        right = len(values)

        while left+1 != right:
            m = (left+right)//2
            
            v = values[m]
            
            if v[0] == timestamp:
                return values[m][1]
            elif v[0] > timestamp:
                right = m
            else:
                left = m
                
        if values[left][0] <= timestamp:
            return values[left][1]
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
