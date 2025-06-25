from typing import (
    List,
)

class Solution:
    """
    @param heights: An integer array
    @return: Indexs of buildings with sea view
    """
    def find_buildings(self, heights: List[int]) -> List[int]:
        """
        Revisited 6/25/2025
        https://www.lintcode.com/problem/3714/
        Time: O(N)
        Space: O(N)

        similar to trapping rain water,
        using a prefix and suffix array, where you track all the max heights found so far
        starting from the left for prefix, and starting from the right for suffix

        In this case, it's simplified since we only care about the max elements to the right, basically saying
        is there an element on the right that is greater than the current element I'm at?

        [5, 2, 3, 4]

        finding the suffix for the max elements on the right side 

        suffix = [5, 4, 4, 4]

        in this case, there's nothing to the right of index 3, so this has an ocean view
        for index 2, 3 < 4, so it does not have an ocean view 
        for index 1, 2 < 4, so it does not have an ocean view 
        for index 0, 5 > 4, so it does have an ocean view 

        another example:
        [5, 4, 6, 3]

        suffix = [6, 6, 6, 3]

        notice that because there's a 6 at index 2, the new max that was found is now 6,
        so that continues down to index 0. In this case, only index 3 would have an ocean view since
        at index 0, the 5 gets blocked by the 6 at index 2
        """

        suffix = [height for height in heights]
        res = []
        # starting from the back, ignoring the last element of the list (since there's nothing to the right )
        for i in range(len(suffix)-2,-1,-1):
            # take the max of the current element and the previous element (in this case, i + 1 since we're going backwards ) 
            suffix[i] = max(suffix[i], suffix[i+1])
        for i in range(len(heights)-1):
            if heights[i] > suffix[i+1]:
                res.append(i)
        res.append(len(heights)-1)
        return res