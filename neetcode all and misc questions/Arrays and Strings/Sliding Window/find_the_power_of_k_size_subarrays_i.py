class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        """
        https://neetcode.io/solutions/find-the-power-of-k-size-subarrays-i

        when looking at a subarray, the next index's value must be +1 of the previous

        brute force:
        can do a nested for loop approach where we iterate through each element
        of K sized subarray, check for ascending consecutive. 
        This is O(N*K) though, and we're bottlenecked due to repeated work.
        whenever we check the next K sized subarray, we're re-examining two of the same
        elements as before.

        Optimization:

        example: 1 2 3 4 3 4 5
        sliding window:

        initially, what we do as check if the previous element is -1 of the current,
        then we keep a counter that tells us the current count of consecutive elements
        when we exceed K, move the left pointer by 1. Then check if this element at the left pointer
        was a consecutive element by checking if the element in front is +1, if so, decrement
        from the count of consecutive elements.

        The key here is that because we're cumulatively checking whether the current element is +1 from the previous,
        we know that we're in a consecutive sequence as long as the count of consecutive elements == K
        
        To check whether we save a max element or not, we check to see if the counter
        of consecutive elements == K,
        so by default, we'd save the last element in the sequence as the max

        1 2 3
        our current count is 3, we save 3
        1 2 3 4, we've exceeded k, so increment left pointer and remove one consecutive 
        element from the count
        however, we see that the current is 4, so previous is 3, therefore, we add 
        one consecutive element to the count
        count = 3,
        count == K, so we save 4
        2 3 4
        2 3 4 3, remove one element from the left
        3 4 3, since the current element is not consecutive (3), we don't add to the count
        count = 2, count != K, so we save a -1
        3 4 3 4, remove left most pointer, which is one consecutive
        count = 1
        4 3 4, the current element is consecutive, so we add 1
        count = 2
        4 3 4 5, left most pointer is NOT consecutive (because 4 > 3), so we remove
        it but don't decrement
        count = 2, count != K, so we save a -1
        3 4 5, the current element (5) is consecutive, so we increment
        count = 3
        count == K, so we save 5
        
        """
        # if there is only one element in the array, or
        # the k == 1 (which means every element is a consecutive element with itself),
        # just return the array
        if len(nums) <= 1 or k == 1:
            return nums
        # the default always starts at 1 since a single element is considered consecutive with itself
        count = 1
        res = []
        l = 0
        for r in range(1, len(nums)):
            # if we've exceeded the length of the window,
            # check if we're removing a consecutive element at the left most pointer
            # before incrementing the left
            if (r - l + 1) > k:
                if nums[l] + 1 == nums[l+1]:
                    count -= 1
                l += 1
            # if the current element is +1 greater than the previous
            if nums[r-1] + 1 == nums[r]:
                count += 1
            
            # if our right pointer is at least k-1,
            # and count of consecutive elements is K,
            # that means we're in a consecutive sequence of K, so by default,
            # the max is the last element in this sequence
            # otherwise, we append -1
            if r >= k-1:
                res.append(nums[r] if count == k else -1)
            
        return res
