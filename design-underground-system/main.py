from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.users = defaultdict(tuple)
        self.ways = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.users[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, st = self.users[id]
        self.ways[(start, stationName)].append(t - st)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        vs = self.ways[(startStation, endStation)]

        return sum(vs) / len(vs)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
