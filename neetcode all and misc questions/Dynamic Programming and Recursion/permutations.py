'''
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]

https://leetcode.com/problems/permutations/

Concept:
Within our recursion, loop through our list of nums
we pick nums[i], and then pass in a list of all the elements except the one that we picked
so that we only permute on the remaining numbers, and also keep track of a separate variable
that will have our current permutation so far in a list (called "so_far")

eventually we will pass an empty list into the function call, in that case, just append
our current permutation into our total.

During the backtracking, the current permutation will then look for a different number to permute

'''
class Solution3:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Revisited on 10/6/2024 with a similar solution as below
        """
        self.res = []
        def search(searchSpace, cur):
            if len(searchSpace) == 0:
                self.res.append(cur)
                return
            for i in range(len(searchSpace)):
                search(searchSpace[:i]+searchSpace[i+1:], cur + [searchSpace[i]])
            
        search(nums, [])
        return self.res
"""
Revisited on 8/4/2023
Same concept as above, but a slightly shorter solution that populates 
a set (still an accepted solution despite the return type not being a list)
"""
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = set()
        def helper(nums, cur):
            if len(nums) == 0:
                self.res.add(tuple(cur))
                return
            for i in range(len(nums)):
                helper(nums[0:i]+nums[i+1:], cur + [nums[i]])
        helper(nums, [])           
        return self.res

class Solution:
    ## time complexity is O(N!) (factorial) (or is it O(N*N!))? since the list slicing could be O(N)
    ## space is also O(N!) to keep track of all different permutations
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.search(nums, [], [])
    def search(self, nums: List[int], so_far: List[int], total : [int]) -> List[List[int]]:
        if (not nums):
            ## if the nums list is empty, we've finished picking one permutation
            ## so append this to our total list
            total.append(so_far)
        else:
            for i in range(len(nums)):
                pick = nums[i]
                ## we can only permute on the rest of the remaining numbers
                ## so pass in a list of all the elements except the one we picked
                self.search(nums[:i]+nums[i+1:], so_far + [pick], total)
        ## at the end just return our total list which should now contain all of our permutations
        return total
    '''
    nums = [1,2,3]
    self.answer = []
    self.search([1,2,3],[])
    first call
    pick = 1
    self.permute([2,3], [1])
    
    second call
    pick = 2
    self.permute([3], [1,2])
    
    third call
    pick = 3
    self.permute([], [1,2,3])
    
    fourth call
    (base case, empty nums)
    self.answer.append([1,2,3])
    
    backtrack to third call
    nothing to pick
    
    backtrack to second call
    we can pick 3 here in the next iteration of our for loop
    self.permute([2], [1,3])
    
    fifth call
    pick 2
    self.permute([], [1,3,2])
    
    base case is found
    self.answer.append([1,3,2])
    
    backtrack to fifth call
    nothing left to pick in the loop,
    
    backtrack to second call
    nothing left to pick here
    
    backtrack to first call
    pick 2
    self.permute([1,3], [2])
    
    ...
    '''