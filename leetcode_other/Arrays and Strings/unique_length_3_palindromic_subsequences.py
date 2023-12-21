class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        """
        
        c a b c a
        start from the mid? at b
        
           a b c
        neither side is a palindrome, move one more to the right
        a b a, one palindrome found, put it in set so we don't double count it
        
        c a b c a
        
        can also try moving one more left
        c b c
        
        c a b d c
        """
        """
        Brute Force
        """
        # unique = set()
        # for i in range(1, len(s)-1):
        #     l = i - 1
        #     r = i + 1
        #     while l >= 0 and r < len(s):
        #         leftVal = s[l]
        #         rightVal = s[r]
        #         newL = l
        #         newR = r
        #         if leftVal == rightVal:
        #             unique.add(s[l] + s[i] + s[r])
        #         # continuously check the right side
        #         while (newR < len(s)-1):
        #             newR += 1
        #             if s[newR] == s[l]:
        #                 unique.add(s[l] + s[i] + s[newR])
        #         # continuously check the right side
        #         while (newL > 0):
        #             newL -= 1
        #             if s[newL] == s[r]:
        #                 unique.add(s[newL] + s[i] + s[r])       
        #         l -= 1
        #         r += 1
        # return len(unique)
        """
        Optimal Solution (Neetcode)
        Key Concepts:
        1) When doing a string problems that only use letters of the alphabet,
        always remember that there's 26 characters max in the alphabet and see if you can use
        that fact to solve the problem.
        2) In palindromes of length 3, the character to the left of the middle and the character to the right of the middle have to be the same. We can use this fact by simply looping through and treating each
        s[i] as a "middle", and then seeing if it's possible that any character on the left of middle,
        and any character to the right of middle can be the same.
        
        Time: O(26 * N)
        
        example:
        
        s = "bbcbaba"
        
        answer = 4
            
        right = {a: 2, b: 4, c: 1}
        left = set()
        res = set()
        
        i = 0
        b 
        decrement b from right
        {a: 2, b: 3, c: 1}
        
        from a ... z, 
        because left is empty, we can't make a length three palindrome here,
        so add b to "left" and go onto the next iteration
        
        i = 1
        b
        left = {b}
        res = set()
        decrement b from right
        right = {a: 2, b: 2, c: 1}
        
        from a ... z,
        b is present in both left and right, so we can make a length three palindrome here,
        add bbb to our res set
        res = {bbb}
        
        adds b to left, it already exists, move onto the next iteration
        
        i = 2
        c
        decrement c from right, and pops c out since the value becomes 0 
        right = {a: 2, b: 2}
        
        from a ... z,
        b is present in both left and right, so we can make a length three palindrome,
        add bcb to our res set
        res = {bbb, bcb}
        
        ...
        
        
        
        """
        from collections import Counter
        res = set()
        # initially left side is empty
        left = set()
        # right side contains all the characters of S
        right = Counter(s)
        for i in range(len(s)):
            # middle of our palindrome
            mid = s[i]
            # because we're evaluating this character in the middle,
            # we want to remove this from the possible list of chars on the right 
            right[mid] -= 1
            if right[mid] == 0:
                right.pop(mid)
            
            for j in range(26):
                # ASCII math, this will convert our index
                # to it's appropriate alphabet character
                # based on the fact that there's 26 possible letters,
                # so 0 = a, 1 = b, 2 = c, 25 = z, etc
                c = chr(ord("a") + j ) 
                # if c in left and c in right, that means a 3 length palindrome can be created
                # since the characters would be the same here
                if c in left and c in right:
                    res.add(c + mid + c)
            
            # after we evaluate the middle, it is now going to be in the left portion
            left.add(mid)
        return len(res)