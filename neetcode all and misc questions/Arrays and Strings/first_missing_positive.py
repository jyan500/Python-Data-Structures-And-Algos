class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        Note: this is not the most optimal solution (the optimal one uses O(1) space
        by modifying the input array)
        https://leetcode.com/problems/first-missing-positive/description/
        O(N) Time
        O(N) Space 
        Using a set of only the positive numbers of the nums array,
        loop through the numbers 1 ... max(nums) and check if starting from 1, 
        which number is not present in the set

        if we've iterated through all the onlyPositives, in the case that array
        was empty, that means everything was < 0, so we'd just return 1,
        otherwise return max(nums)+1, as this means every consecutive number from 
        1 ... max(nums) was present in the onlyPositives array
        """
        ref = []
        onlyPositives = set(filter(lambda x: x > 0, nums))
        for i in range(1, max(nums)+1):
            if i not in onlyPositives:
                return i
        return 1 if max(nums)+1 <= 0 else max(nums)+1 

            