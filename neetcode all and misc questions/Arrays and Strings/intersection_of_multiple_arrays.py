"""
https://leetcode.com/problems/intersection-of-multiple-arrays/
To find the elements that are in common between multiple arrays,
1) keep an initial set by converting the first nested list into a set
2) for each nested array 1 ... n-1, convert each array into a set. 
And then take the intersection between the result of the previous intersection,
and the current set.
3) Turn the result back into a list and sort

Time: O(N*M) + O(NLogN), O(N*M) because within each nested array, we need to convert it to a set, and also find the intersection,
which is O(M) work, depending on the shorter of the two sets being compared.
Space: O(M), where M is the longest nested list, since the final result can only be as long as the longest nested list in the array
"""
class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        res = set(nums[0])
        for i in range(1, len(nums)):
            curSet = set(nums[i])
            res = res.intersection(curSet)
        res = list(res)
        return sorted(res)