"""
LC Premium Problem
https://www.lintcode.com/problem/905/?utm_source=%5B%27sc-bky-zy%27%5D
Approach:
1) Because we don't know how deep the nested lists are, run a DFS initially
to get the max depth. At the same time, we also store the elements at each depth in a dictionary
for later calculation

2) Once we have the max depth, we run a loop starting from max depth ... -1, and have a counter
"reverseDepth" starting from 1. The idea is that we start from the max depth first, and then multiply
that by the "reverseDepth" of 1, and then increment reverseDepth. This way, we increase the 
amount that we multiply by as we travel from the leaf depth all the to the base.

Time:
O(N) + O(N^H), where H is the level of nesting, and N is the amount of elements in the array

Space:
O(M), where M is the amount of integers in the array, since we're creating the hashmap to store all the integers
at each depth
"""
class Solution:
	def reverseNestedListWeightSum(self, nestedList):
		from collections import defaultdict
        self.maxDepth = float("-inf")
        self.elements = defaultdict(list)
        def findMaxDepth(curList, depth):
            for i in range(len(curList)):
                if type(curList[i]) == list:
                    findMaxDepth(curList[i], depth+1)
                else:
                    self.elements[depth].append(curList[i])
            self.maxDepth = max(depth, self.maxDepth)
        findMaxDepth(nestedList, 1)
        reverseDepth = 1
        curSum = 0
        for i in range(self.maxDepth, -1, -1):
            curSum += reverseDepth * sum(self.elements[i])
            reverseDepth += 1
        return curSum

if __name__ == "__main__":
	s = Solution()
	ans = s.reverseNestedListWeightSum([[1,1],2,[1,1]])
	assert(ans == 8)
	ans2 = s.reverseNestedListWeightSum([1,[4,[6]]])
	assert(ans2 == 17)

"""
Lintcode solution uses a NestedInteger Interface that implements the following methods:
getInteger() -> gets the integer
getList() -> gets the list
isInteger() -> returns true if integer, false if not

from collections import defaultdict
self.maxDepth = float("-inf")
self.elements = defaultdict(list)
def findMaxDepth(curList, depth):
    for i in range(len(curList)):
        if not curList[i].isInteger():
            findMaxDepth(curList[i].getList(), depth+1)
        else:
            self.elements[depth].append(curList[i].getInteger())
    self.maxDepth = max(depth, self.maxDepth)
findMaxDepth(nestedList, 1)
reverseDepth = 1
curSum = 0
for i in range(self.maxDepth, -1, -1):
    curSum += reverseDepth * sum(self.elements[i])
    reverseDepth += 1
return curSum
"""

