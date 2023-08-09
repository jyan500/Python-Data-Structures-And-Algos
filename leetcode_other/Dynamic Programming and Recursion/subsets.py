"""
This is a very similar concept to partition equal subset sum,
where the recursive relation is a knapsack

Time Complexity: O(2^N)
https://leetcode.com/problems/subsets/discuss/855802/Java-Backtracking-2n-100-fast-solution-Time-Complexity-Explained.

1) knapsack relation
we either pick A and continue by incrementing i
or we don't pick A and continue by incrementing i
base case is if i reaches the end of the list
Note that we need to remove (cur) once both recursive calls finish,
otherwise we end up with duplicate elements. For example, [1, 2]
initially cur = [], i = 0

1) first call 
append cur, empty list
knapsack(0 + 1, cur + [1])
cur = [1], i = 1

2) second call 
append cur, [1]
knapsack(1 + 1, cur + [2])
cur = [1, 2], i = 2

3) third call, 
append cur, [1, 2]
base case, i == len(nums), returns
back to the second call

4) fourth call
(1+1, cur)
cur = [1], i = 2
append [1], but we reach the base case again
we already added [1] in a previous call, so we can just remove it now
that both paths have already been explored starting from second call

5) Goes all the way back to the first recursive call, second recursive case
cur = [], i = 1
knapsack(0 + 1, [])

6) fifth call
append([])
knapsack(1+1, cur + [2])

7) sixth call
cur = [2], i = 2
append([2])
base case i == len(nums), returns

8) back to the fifth call, second recursive case
knapsack(1+1, cur)

9) seventh call
appends([]), i = 2
base case reached, i == len(nums), returns

10) back to the fifth call, but both paths are finished, we need to remove
cur which is the empty list so it doesn't get duplicated

Final result: [[], [1], [1,2], [2]]
        
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def knapsack(i, cur):
            self.res.append(cur)
            if i == len(nums):
                return
       
            knapsack(i+1, cur + [nums[i]])
            knapsack(i+1, cur)
            self.res.remove(cur)
            
        knapsack(0, [])
        return self.res