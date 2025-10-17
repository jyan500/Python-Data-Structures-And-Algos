class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        https://leetcode.com/problems/number-of-ways-to-split-array/
        
        Time: O(N)
        Space: O(N)

        save the accumulated sums in the array per index
        this way, to figure out whether a valid split occurs:
        take the current index's sum, and then subtract it from
        the value of the last index. The last index would be the accumulated sum
        for the whole array, so if you subtract the current index's value,
        that would be equal to the sum of everything to the right of the current index.

        For example:
        [10, 4, -8, 7]
        the prefix version is 
        [10, 14, 6, 13]

        if you were to split the array between index 1 and index 2 for example:
        14 is the total sum up to index 1 (which is the left half)
        13 - 14 = -1 would be the total sum from index 2 to index 3 (which is the right half)

        therefore 14 >= -1, so this is valid

        therefore, you would just need to iterate through the array another time to
        compare each i, where value[i] >= (value[-1] - value[i]), up to n - 1
        """
        prefix = nums.copy()
        for i in range(1, len(prefix)):
            prefix[i] = prefix[i-1] + prefix[i]
        res = 0
        # don't count the last index because that's not considered a valid split
        # according to the problem, since there must be at least one element to the right of i
        for i in range(len(prefix)-1):
            if prefix[i] >= (prefix[-1] - prefix[i]):
                res += 1
        return res