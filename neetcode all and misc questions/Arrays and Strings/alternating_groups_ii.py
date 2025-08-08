class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        """
        [0 1 0 0 1 0 1] k = 6
               ^     ^
        0 1 0 1 + the first two positions (0 1)

        in order to test every window from i ... N - 1, since you need to test the elements prior to
        i, you can double the amount of elements in colors
        [0 1 0 0 1 0 1] [0 1 0 0 1 0 1]
               
        and run a sliding window where we have a prev value, and we're constantly checking 
        if the prev is alternating with the cur. 
        If so:
            we continue until we reach
            a window of size k and increment our res. 
        else:
            we can just shift our left pointer all
            the way to the right pointer. Since we are not able to make an alternating
            sequence with any of the previous characters
            i.e 
            0 1 0 0
            ^     ^
            l     r 
            if we have this window that's not alternating, if we were to shift l += 1,
            and start testing, we'd end up with another non-alternating window since indices
            2 and 3 are not alternating.

        one important note is that when we're running the sliding window
        """
        N = len(colors)
        allWindows = colors + colors
        res = 0
        def isAlternating(x, y):
            return (x == 0 and y == 1) or (x == 1 and y == 0)
        l = 0
        prev = allWindows[0]
        for r in range(1, len(allWindows)):
            # note that if we have a left pointer that exceeds the original size of colors array, 
            # that means we've already checked past the
            # threshold of elements necessary (even if they are looping around), so we need to stop here.
            # otherwise, we'd start potentially checking repeated sequences
            if l >= N:
                break
            if not isAlternating(prev, allWindows[r]):
                # if not alternating, we can just set l directly to where r is,
                # since we cannot make an alternating sequence with any of the previous characters up to this point.
                l = r
                # set the prev to the current element, we start testing from the next
                # pointer onwards (i.e l = r, and r = r + 1)
                prev = allWindows[l]
            else:
                # if we've reached an alternating sequence of size k, we can shift the left pointer
                # by one and see if we can find another sequence
                if r - l + 1 == k:
                    l += 1
                    res += 1
                prev = allWindows[r]    
        return res

