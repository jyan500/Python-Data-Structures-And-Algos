class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        """
        Approach: 
        keep a hashmap that corresponds with sliding window with left and right pointers
        if the value we want to add has a count that exceeds k, the shift the left pointer 
        decrement the count in the hashmap based on the value at the left pointer

        this ensures that our window always has values where the count <= k
        keep the max length by taking max(r-l+1, maxLength) at each iteration

        Time: O(N)
        Space: O(N)

        """
        from collections import defaultdict
        l = 0
        counter = defaultdict(int)
        maxLength = 1
        for r in range(len(nums)):
            # if adding the current value would cause its count > k
            # we shift the window until we find the last occurrence
            # of nums[r], and decrement from nums[l]
            if counter[nums[r]] + 1 > k:
                while (nums[l] != nums[r]):
                    counter[nums[l]] -= 1
                    l += 1
                # once we've found the element to remove, increment once more
                counter[nums[l]] -= 1
                l += 1
            maxLength = max(r-l+1, maxLength)
            counter[nums[r]] += 1
        return maxLength