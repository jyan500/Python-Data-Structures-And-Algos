class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """
        because the array is circular, 
        you should be able to examine a subarray of length nums like so
        [1, -2, 3, -2] -> [1, -2, 3]
        imagining if the -2 "wraps around" back to index 0, 
        you can examine [-2, 1, -2, 3]

        a brute force solution would be checking every possible subarray sum,
        making sure to include the extra segment from [0: n-1] at the end of the array
        to simulate the wrap-around

        Optimization:

        Apply Kadane's algorithm + Prefix and Suffix sums
        Kadane's algorithm will give you the max sum subarray within the middle of the array, 
        and then you can utilize the sum of the prefix and suffix sum at i to get the surrounding "circular"
        subarray. This way, you're always examining the max between the subarray in the middle, and then the surrounding "circular" subarray
        that wraps around
        """

        # get the prefix and suffix sums so you know at each i, what's the max subarray
        # you can make from 0 ... i for the prefix, and from i ... n - 1 for the suffix
        prefix = len(nums) * [0]
        suffix = len(nums) * [0]
        prefixSum = nums[0]
        suffixSum = nums[-1]
        suffix[-1] = nums[-1]
        prefix[0] = nums[0]
        for i in range(len(suffix)-2,-1,-1):
            suffixSum += nums[i]
            suffix[i] = max(suffix[i+1], suffixSum)
        for i in range(1, len(prefix)):
            prefixSum += nums[i]
            prefix[i] = max(prefix[i-1], prefixSum)
        
        # apply kadane's algorithm, and at each i, compare whether it's better to take
        # the subarray starting from i, or to take the surrounding circular
        # max subarray after i + the max subarray before i
        curMax = 0
        res = nums[0]
        for i in range(len(nums)):
            # if the current number exceeds the sum so far, "restart" fresh by resetting the curMax to nums[i]
            curMax = max(curMax+nums[i], nums[i])
            res = max(curMax, res)
            # now we need to check whether it's better to take this subarray in the middle
            # or the surrounding circular one
            if i > 0 and i < len(nums)-1:
                res = max(prefix[i-1]+suffix[i+1], res)
        return res

