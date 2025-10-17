class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/number-of-zero-filled-subarrays/
        
        Time: O(N)
        Space: O(N)

        0 0 0 - 1 count of 3 0's
        2 count of 2 0's
        3 count of 1 0's

        0 0 0 0 - 1 count 4 0's
        2 count 3 0's
        3 count of 4 0's
        4 count of 1 0's

        10

        so the pattern here is that the total amount of zero filled subarrays
        inside a given subarray follows the arithmetic series, (n(n+1))/2

        the algorithm is to find all the subarrays of contiguous zeroes.
        And then apply the arithmetic series where n is the length of the subarrays to
        each of the subarrays in order to figure out the count of the smaller subarrays
        inside that subarray as shown above.
        """
        lengths = []
        curLength = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                curLength += 1
            else:
                # reset the length of the current window once its no longer valid
                lengths.append(curLength)
                curLength = 0
        # if the array ends with a zero subarray, need to add to the lengths array
        if curLength > 0:
            lengths.append(curLength)
        for i in range(len(lengths)):
            res += int((lengths[i] * (lengths[i] + 1))/2)
        return res