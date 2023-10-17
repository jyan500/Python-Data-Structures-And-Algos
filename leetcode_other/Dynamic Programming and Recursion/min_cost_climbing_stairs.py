"""
https://leetcode.com/problems/min-cost-climbing-stairs/
Concept:

1) The recurrence relation is that you want the minimum between the cost 
of going to the ith + 1 staircase (climbing one stair) or
ith + 2 staircase (climbing 2 stairs)

2) Run two cases, where you start on i = 0, and another on i = 1

3) Base Case: the "top" of the staircase is i >= len(cost), so if you've exceeded
this, there's no need to pay anymore to climb, so return 0

4) Memoize the minimum amount of pay needed at a given step to reuse these results later

Time complexity:
O(N)

Space Complexity:
O(N)

"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.memo = dict()
        def helper(i):
            if i in self.memo:
                return self.memo[i]
            if i >= len(cost):
                return 0
            self.memo[i] = cost[i] + min(helper(i+1), helper(i+2))
            return self.memo[i]
        
        return min(helper(0), helper(1))
            