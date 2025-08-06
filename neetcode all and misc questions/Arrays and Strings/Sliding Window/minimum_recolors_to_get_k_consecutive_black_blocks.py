class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """
        https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

        O(N) Time
        O(1) Space

        need to get a consecutive row of black blocks of length K
        by changing W to B blocks. Find the minimum amount of 
        changes needed in order to get that proper length row of black blocks.

        Use a sliding window
        if you see a "W", change it to a B, increment 
        blocks = WBBWWBBWBW k = 7

        r = 0 W changes to B, increment count by 1
        r = 1 already a B
        r = 2 already a B
        r = 3 W changes to B, increment count to 2
        r = 4 W changes to B, increment count to 3
        r = 5 already a B
        r = 6 already a B, at this point, our window is now 7.
        We can now increment the left pointer until we reach the next "B" block,
        and if there are any "W" blocks along the way, decrement the count 
        since its outside of the window and we're not changing that to a "B" block anymore.

        l should now be 1, decrement count by 1 (Back to 2) since l = 0 was a "W" block, the window is now 6 again
        r = 7, W changes to a B, increment count to 3
        we're back at length 7 again, so have to slide the window until it reaches
        the next B block.

        l should now be 2, we don't need to decrement this time since l = 1 was a "B" block

        r = 8, is a B block (length 7), repeat the same steps above...
        l is now at 3

        """
        l = 0
        count = 0
        minCount = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == "W":
                count += 1
            # if we reach a window count of k of only black blocks,
            # calculate the min count
            # shift the left pointer by one to slide the window
            # if the left pointer was pointing at a white block before, decrement from the overall count of operations
            # since it falls outside the current window
            if r - l + 1 == k:
                minCount = min(minCount, count)
                if blocks[l] == "W":
                    count -= 1
                l += 1
        return minCount
            