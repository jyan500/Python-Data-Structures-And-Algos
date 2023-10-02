'''
Combination Sum IV
https://www.youtube.com/watch?v=GWqe_xfqxCA&ab_channel=AlgorithmsMadeEasy
https://leetcode.com/problems/combination-sum-iv/discuss/220985/Simple-Python-DP-Solution-Top-Down-Approach
https://www.youtube.com/watch?v=dw2nMCxG0ik&ab_channel=NeetCode

The intuition behind this problem is to draw out a tree, were we choose one value, and subtract the target
value off of the number we chose. Then we loop through the list of numbers and continually choose 
a number (which creates the tree) until our target == 0, at that point we have found a combination of numbers. At this point,
increment the total. The recursion will then backtrack until it can find another point when target == 0

Without optimization, this solution is exponential (O(N^M)) 

In terms of optimization, we can use memoization to store repeated subproblems. For example, if our target is 1,
we know that no matter what combination of numbers created this target of 1, the total amount of combinations that can
be made at that point will always be the same. 

final time complexity of memoized solution is O(N*M), where N is the length of nums, and M is the amount of times we need
to try each number per target value (since no matter what our target is, we still need to perform the "for num in nums" loop)

space complexity is also O(N), which is the cost of the hashmap 
'''

"""
Revisited 10/2/2023
slightly different solution where we add up a running total and see if it equals target

example:
[1, 2, 3], target = 4

Starting with 1st value: 1
1st combination tried: 1, 1, 1, 1, where the cur is 3
when the cur is 3 (1, 1, 1), there's one way to get to 4, stores in the memo
self.memo = {3: 1}

2nd combination: 1, 1, 2, where the cur is 2
when the cur is 2, there's two ways of getting to 4 (1, 1, 2 OR 1, 1, 1, 1), 
self.memo = {3: 1, 2: 2}

3rd combination 1, where the cur is 1
4 different ways (1, 1, 1, 1 OR 1, 2, 1 OR 1, 3 OR 1, 1, 2)

Starting with 1st value 2:

2, when cur is 2, we already know that there's two ways of getting to 4 based 
on the memo, so we recall the memo's results (2)

when cur is 3, we already know that there's one way of getting to 4, so we
recall memo's results (1)

4 + 2 + 1 = 7




"""
class Solution2:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        self.memo = dict()
        def helper(cur, target):
            if cur in self.memo:
                return self.memo[cur]
            if cur == target:
                return 1
            if cur > target:
                return 0
            else:
                res = 0
                for i in range(len(nums)):
                    res += helper(cur + nums[i], target)
                self.memo[cur] = res
                return res
        res = 0   
        for i in range(len(nums)):
            res += helper(nums[i], target)
        return res

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = dict()
        def search(target: int) -> int:
        	## note I was using memo.get(target) beforehand and this was causing TLE
            if (target in memo):
                return memo[target]
            elif (target == 0):
                return 1
            else:
                total = 0
                for num in nums:
                    if (num <= target):
                        total += search(target - num)       
                ## whenever we're successful in finding a target that adds up to the total, store it inside memo
                memo[target] = total
                return total
        return search(target)