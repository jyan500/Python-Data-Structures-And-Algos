"""
https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/
https://www.youtube.com/watch?v=MOeuK6gaC2A&ab_channel=NeetCode
Key Concepts:
 Sliding Window (Modified)
- There's a clever way around to type-1 operation stated in the problem (remove a character at the start of string and appending it),
 to make the sliding window method easier by appending the string to itself:
 From:
 1 1 1 0 0 0
 To:
 1 1 1 0 0 0 1 1 1 0 0 0

 This way, once we run our "type-1" operations, we simply need to look at the next character in our string

- to tell the amount of flips needed, we just need to compare two versions of alternating strings to our current string and increment
the amount of differences. 
 -Once we've reached the length of our sliding window, we see if the left most element caused a difference, if so we can
decrement the amount of differences

Time Complexity: O(N)
Space: O(N) (technically for building the target strings of length N)
"""
class Solution:
    def minFlips(self, s: str) -> int:
        """
        1) Try doing all type 2 operations without doing any type 1 operations first
        2) Then try a type 1 operation, followed by another, etc And then between those,
        try doing type 2 operations again.
        
        1001110
        
        Only type-2 operations:
        From 1001110 to 
        1010101 requires 5 operations
        
        0101010 requires only 4 operations, so minimum is 4 here
        
        Try one type-1 operation:
        1001110 to 0011101
        
        requires 3 type-2 operations
        1010101
        
        0101010 requires 6 type-2 operations (too many)
        
        Try another type-1 operation:
        0011101 becomes 0111010
        
        0101010 requires only 1 operation (this is probably the answer)
        
        1010101 requires 2 operations 
        
        Some patterns/potential for optimization (From Neetcode)
        If you've already calculated the min amount of flips for string i ... n,
        and then you do one type one operation shifting the first element to the last,
        you only need to account for the addition of the last element, this is where the
        sliding window comes in.
        0 0 1 1 1 takes two operations to flip to 1 0 1 0 1
        0 0 1 1 1 shifts to 0 1 1 1 0, we've already done the operations for 0 1 1 1
        """        
        def buildAlternatingString(startingChar, length):
            res = startingChar
            if startingChar == "1":
                for i in range(1, length):
                    res += "0" if i % 2 != 0 else "1"
            else:
                for i in range(1, length):
                    res += "1" if i % 2 != 0 else "0"
            return res
    
        # clever trick: so we don't have to pop a string off and append each time,
        # we can concatenate string s to itself, so that way, after we've gone through
        # all type one operations, we'll end up with the same string as before in our sliding window
        n = len(s)
        s = s + s
        target1 = buildAlternatingString("1", len(s))
        target2 = buildAlternatingString("0", len(s))

        l = 0
        r = 0
        target1amt = 0
        target2amt = 0
        res = float("inf")
        while (r < len(s)):
            # if the character is different from the target string,
            # this means it would need to be inverted, so increment by one
            if s[r] != target1[r]:
                target1amt += 1
            if s[r] != target2[r]:
                target2amt += 1
            # if our sliding window has exceeded the length of the original string,
            # that means we need to do a "type one" operation by identifying the next character
            if (r - l + 1) > n:
                # remove the first char and treat it as the "new" element in the window
                # if the first char was differing, remove it if it's no longer a difference
                if s[l] != target1[l]:
                    target1amt -= 1
                if s[l] != target2[l]:
                    target2amt -= 1
                
                l += 1
            
            # once we've done all of our operations for this window, check to see if we have
            # a new minimum
            if (r - l + 1) == n:
                res = min(res, target1amt, target2amt)
            r += 1
                    
        return res
                
                
        
        
        
            
            
            
        
        
        
        
        