"""
https://leetcode.com/problems/majority-element/
O(N) time O(N) space
 
There's a O(N) Time but O(1) space solution that is called
the Boyer-Moore Majority Vote Algorithm, which seems pretty obscure.
Reference: https://leetcode.com/problems/majority-element/discuss/51613/O(n)-time-O(1)-space-fastest-solution
http://www.cs.utexas.edu/~moore/best-ideas/mjrty/
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for i in range(len(nums)):
            if nums[i] in counter:
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        majority = 0
        maxElement = 0
        for k in counter:
            if counter[k] >= len(nums)/2:
                if counter[k] > majority:
                    majority = counter[k]
                    maxElement = k
        return maxElement