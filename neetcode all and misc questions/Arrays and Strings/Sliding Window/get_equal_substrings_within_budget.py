class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        """
        https://leetcode.com/problems/get-equal-substrings-within-budget/submissions/
        Pattern:
        Sliding Window with an inner while loop to shrink the left side of the window until a
        condition is met
        Time: O(N)
        Space: O(1)
        
        example:
        abczeeeee
        abcaeeeee
        maxCost of 3
        in this example, we can match abc (which is max len of 3 so far), without
        any cost. However, once we reach z, ord(z) - ord(a) is 25, which exceeds our max cost 
        of 3
        
        we have to continually decrease the left side in order to cut cost
        remove a, remove b, remove c, and then remove z, which pushes both pointers to e
        
        then we match e, e, e, e, e with no cost, and see that the max chars matched is now 5
        """
        n = len(s)
        l = 0
        currentCost = 0
        res = float("-inf")
        curLen = 0
        for r in range(n):
            # get the absolute difference between ASCII values of each character on both strings
            cost = abs(ord(s[r]) - ord(t[r]))
            currentCost += cost
            curLen += 1
            # after adding this character, if the cost exceeds our max cost, we continue
            # removing the cost from the left side until we no longer exceed max cost
            # also decrement the length
            while (currentCost > maxCost):
                currentCost -= abs(ord(s[l]) - ord(t[l]))
                l += 1
                curLen -= 1
            # after doing the operations above if necessary, then calculate the maxLen we've achieved
            res = max(curLen, res)
        return res
            
            