# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.res = []
        for nl in nestedList:
            self.res.extend(self._unfold(nl))
        self.l = len(self.res)
        self.cur = 0
                
    def _unfold(self, nl: NestedInteger) -> List[int]:
        r = []
        if nl.isInteger():
            r.append(nl.getInteger())
        else:
            nestedList = nl.getList()
            for n in nestedList:
                v = self._unfold(n)
                r.extend(v)
        return r
    
    def next(self) -> int:
        if self.cur < self.l:
            v = self.res[self.cur]
            self.cur += 1
        else:
            v = None
        return v
    
    def hasNext(self) -> bool:
        if self.cur < self.l:
            return True
        else:
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
