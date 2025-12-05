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

"""
O(N) Time
O(N) Space
pre-flatten the list first,
and then just keep the length of the flattened list,
and current index as class variables for use
in the iterator methods
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flattened = self.flatten(nestedList)
        self.length = len(self.flattened)
        self.i = 0
    """
    algorithm for list flattening:
    recursive, store array
    loop through nested list
        if integer:
            append to array
        else:
            recur down with the nested list, extend to the array so each
            element in the child result list gets appended to the array 
            instead of the child result list itself
    return array
    """
    def flatten(self, nestedList: [NestedInteger]) -> [int]:
        res = []
        for nestedInteger in nestedList:
            if nestedInteger.isInteger():
                res.append(nestedInteger.getInteger())
            else:
                res.extend(self.flatten(nestedInteger.getList()))
        return res

    def next(self) -> int:
        val = self.flattened[self.i]
        self.i += 1
        return val
    
    def hasNext(self) -> bool:
        return self.i < self.length

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())