'''
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

 

Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

Example 4:

Input: candidates = [1], target = 1
Output: [[1]]
Example 5:

Input: candidates = [1], target = 2
Output: [[1,1]]

https://stackoverflow.com/questions/49773957/confusing-about-passing-list-in-recursion-function-of-python

Update to this point ^^: you can concatenate an array to an existing one to create a new array and avoid
the issues caused due to pass by reference (where you append, and then have to pop out like in the first solution)

Time Complexity: O(2^target) exponential

Revisited 4/4/2025
'''
class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        self.res = []
        self.N = len(nums)
        def search(i, curSum, cur):
            if curSum == target:
                self.res.append(cur)
                return
            elif i >= self.N or curSum > target:
                return
            # keep picking the same number until
            # you're at the end of the list, or the cur sum exceeds target sum
            search(i, curSum + nums[i], cur + [nums[i]])
            # move onto the next index, and then repeat the process for that next index and so on
            search(i+1, curSum, cur)
        search(0, 0, [])
        return self.res

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        return self.combinationSumHelper(candidates, target, 0, [], [])
        
    def combinationSumHelper(self, candidates, target, index, cur = [], combinations = []):
        if (target <= 0):
            ## each recursive call, we do target - index to create this base case
            if (target == 0):
                ## make a copy of the cur array to pass in, rather than passing the reference to the cur array
                ## otherwise if you don't make a copy it'll pass in an empty array
                ## on the last recursive call before returning and finishing the entire process, 
                ## since cur = [] at the end of the process, so the values that are within combinations just get turned into empty arrays
                combinations.append(cur[:])
            return
        
        if (index < len(candidates)):
            val = candidates[index]
            cur.append(val)
            ## get the value at the current index and keep repeatedly checking if
            ## combinations of that same number will create a valid combination that adds up to target
            self.combinationSumHelper(candidates, target - val, index, cur, combinations)
            ## if returned from the lowest depth, go one depth before and start seeing
            ## if we can make a combination with the next number in the candidates list
            cur.pop()
            self.combinationSumHelper(candidates, target, index + 1, cur, combinations)
        return combinations
            
        