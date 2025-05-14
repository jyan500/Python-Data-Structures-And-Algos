class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        """
        5/14/2025
        https://www.youtube.com/watch?v=OHZqAc6h3Us&ab_channel=NeetCodeIO
        Binary search on range
        What is the range we want to search on?
        - it's the maximum capability of the robber (how much they can rob)
        lower bound?
        min(nums)

        upper bound?
        max(nums)

        In a helper function, we determine if it's possible for the robber
        to rob k houses and get the capability needed in O(n) Time.
        We can do this by scanning through the nums, if we see a value <= the capability we chose in the range,
            increment count of houses we robbed, and increment index += 2 (like in the house robber problem)
            otherwise, increment index += 1 (since we can't rob this house)
        Note that we're just comparing and seeing how many houses have value <= the chosen capability, which shows
        that they can be robbed.

        Then in binary search, if the helper function returns true and we're able to rob k houses
        and get this capability, we want to search left
        to find a smaller capability value, since the problem states we
        want the minimum capability. Otherwise, we search right.
        """

        lowerBound = min(nums)
        upperBound = max(nums)

        def canRob(capability):
            houses = 0
            i = 0
            while (i < len(nums)):
                if nums[i] <= capability:
                    houses += 1
                    # increment by two since we can't rob adjacent houses, so we have to skip over the next value
                    i += 2
                else:
                    i += 1
            # if we were able to rob at least k houses, return true
            return houses >= k
        
        def binarySearch(l, r):
            mid = l + (r-l)//2
            # if we've exhausted the search space, we should return the last valud value, which should be l,
            # since we were searching left, and l has exceeded r, so l would contain the previous value
            if l > r:
                return l
            # if we can rob k houses with the given capability, we try to find a smaller value
            if canRob(mid):
                return binarySearch(l, mid-1)
            else:
                return binarySearch(mid+1, r)
        return binarySearch(lowerBound, upperBound)
        
