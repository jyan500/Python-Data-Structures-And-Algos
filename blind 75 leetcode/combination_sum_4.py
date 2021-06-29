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