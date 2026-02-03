'''
https://leetcode.com/problems/decode-ways/
https://www.youtube.com/watch?v=W4rYz-kd-cY&list=PLQdWvigIOnscYtuD1UesE2IazI1erKh-W&index=48&ab_channel=Knapsak
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Revisited on 1/30/2026 with a different solution than my attempt in 2023
        backtracking,
    
        1012

        to check whether a given number is in the boundaries
        between A to Z,
        it would be i + ord("A")-1, and then checking
        whether that value is between ord("A") and ord("Z"),
        ord("A") is 65 and ord("Z") is 90
        for example 1 + ord("A") - 1 should be 65, which
        is in bounds 65 <= 65 <= 90

        J -> 10
        A -> 1
        B -> 2

        if we find an invalid cur, for example
        1 -> A
        0 -> this is invalid, since 0 does not map to any character so we backtrack
        10 -> this will go to the case above

        this is different from knapsack, since
        we're interested in just whether at the given
        index, is the current value valid? (rather than
        the current combination of values). It's a partition problem
        rather than a knapsack

        Because we cannot take more than 3 characters 
        (since that would result in a ord(value) of greater than Z),
        we decide at each point whether we want to take 1 or 2 characters,
        and then check their validity

        Can use memoization to optimize from exponential,
        to O(N^2)

        in the memoization state, we would need to check
        whether at a given state index i,
        how many ways can we partition the rest of the characters?
        so essentially, we set memo[i] = res, where res is the 
        amount of ways we can partition starting at index i

        for example:
        "1111"
        if we were to partition this without memoization,
        we would start by calculating
        1
        11
        and then get to either index 1 or index 2
        so at index 2
        if we take 11, we're now at index 3, so we now have a value of 1
        partition 11 , 11, so at memo[3] = 1
        back at index 2
        we can take 1, and be back at index 3,
        but we already know that at memo[3] the best we can do is 1 combination,
        so we just return 1 right away

        going back to index 2
        1 + 1 = 2, so now there are 2 ways
        memo[2] = 2

        back at index 1, once we hit index 2,
        we can then rely on memo[2], 
        and we don't need to recalculate the partitions again


        """
        N = len(s)
        boundary1 = ord("A")
        boundary2 = ord("Z")
        memo = {}
        def search(i):
            # if we made it to the very end, that means that 
            # we were able to successfully break down each character without running
            # into invalid choices
            if i == N:
                return 1
            if i in memo:
                return memo[i]
            takeOne = s[i]
            res = 0
            if i < N - 1:
                takeTwo = s[i] + s[i+1]
                # cannot accept leading zeroes
                if takeTwo[0] == "0":
                    return 0
                valueTakeTwo = int(takeTwo) + boundary1 - 1
                if boundary1 <= valueTakeTwo <= boundary2:
                    res += search(i+2)
            valueTakeOne = int(takeOne) + boundary1 - 1
            if boundary1 <= valueTakeOne <= boundary2:
                res += search(i+1)
            memo[i] = res
            return res

        return search(0)
        
        
class Solution2:
    def numDecodings(self, s: str) -> int:
        """

        With memoization: 
        Time complexity: O(N)
        Space complexity: O(N)

        Revisited on 9/22/2023 with my own solution this time (and passing!)
        recurrence relation:
        1) keep a sliding window i and j, increment by one, where you keep i and j the same values by passing in j+1 for both params i and j, 
        picking individual letters and decoding until you can't pick individuals
        because it doesn't decode to anything (if the individual letter is 0, return 0)
        2) Then try picking two letters this time, starting from i but going to j+1, the next recursive call will then go back to picking individual letters again
        3) If you ever pick two letters and the integer version of it is greater than 26, this is not valid (return 0)
        4) Base Case: if we reach the end of the string, and we weren't stopped by the prior conditions, then we've successfully decoded, return 1 
        5) Use memoization to store the index ranges we've already visited to see how many ways that particular index range i to j can be decoded

        Example:

        2262

        1st recursive call, i = 0 j = 0 pick 2, j + 1
        ------------------------------------------------

        2nd recursive call, i = 1 j = 1, pick 2, j + 1
        ------------------------------------------------

        3rd recursive call, i = 2 j = 2, pick 6, j + 1
        ------------------------------------------------

        4th call, i = 3 j = 3 pick 2, but we've reached the base case because 3 == len(s) - 1, returns 1
        ------------------------------------------------

        back to 3rd recursive call...

        j = 2, pick 62 this time, i = 2 j = 3 

        5th call
        ------------------------------------------------

        this doesn't pass because 62 > 26, return 0
    
        now we pass 1 back to the 2nd recursive call (because 62 can only be decoded in one way)

        back to 2nd call
        ------------------------------------------------

        now we try picking 2 letters here, 26

        i = 1, j = 2

        6th recursive call
        ------------------------------------------------

        going back to picking one letter...

        i = 3 j = 3

        hit the base case, return 1

        going back to the 2nd call... we're now done with the second call 

        1+1 = 2

        returns 2 ***
        ------------------------------------------------

        back to the first call
        ------------------------------------------------

        tries to pick 2 letters (22), where i = 0 and j = 1

        7th call
        ------------------------------------------------

        picks one letter (6)

        i = 2 j = 2

        8th call picks i = 3, j = 3 reaches the base case, returns 1
        ------------------------------------------------

        goes back to the 7th call, tries to do i = 2, j = 3 (62), but fails since 62 > 26...

        7th call is done, returns 1 ***
        ------------------------------------------------

        Bubbles up back to 1st call...

        At the end, it does 2 (see the ***) + 1 (see the ***) = 3 and returns 3

        Final answer = 3
    
        the actual combinations were:
        2 2 6 2 
        2 26 2
        22 6 2


        """
        self.memo = dict()
        def helper(s, i, j):
            if (i,j) in self.memo:
                return self.memo[(i,j)]
            cur = s[i:j+1]
            if cur == "0":
                return 0
            if int(cur) > 26:
                return 0
            if i == len(s)-1 or j == len(s)-1:
                return 1
            self.memo[(j+1,j+1)] = helper(s, j+1,j+1)
            self.memo[(s, i, j+1)] = helper(s, i, j+1)
            return self.memo[(j+1,j+1)] + self.memo[(s, i, j+1)]
        
        return helper(s, 0, 0)

class Solution:
    ## O(N) time and O(N) space solution
    def numDecodings(self, s: str) -> int:
        memo = dict()
        return self.search(s, len(s)-1, memo)
    
    def search(self, s, i, memo) -> int:        
        ## base cases
        
        ## if our index has reached zero, if the number is zero then we cannot decode it
        if (i in memo):
            return memo[i]
        if (i == 0):
            if (int(s[i]) == 0):
                memo[s[i]] = 0
                return 0
            ## otherwise we can decode just the individual digit
            else:
                memo[s[i]] = 1
                return 1
        ## in case the i-2 overshoots, we return 1 in the case of the pair of strings
        if (i == -1):
            return 1
        
        ## two more cases to catch zeros
        ## if our current number is zero, and the previous number can form either a 10 or 20
        if (int(s[i]) == 0):
            if (int(s[i-1]) == 1 or int(s[i-1]) == 2):
                return self.search(s, i-2, memo)
            ## if our current number is zero and the previous number forms a number greater than 20
            ## than we cannot decode this (> 26)
            else:
                return 0
        
        ways = 0
        ## two main cases
        ## we can either choose individual letter (i-1), or we can add the letter onto the previous letter
        ## to form a two digit number (i-2)
        
        ## if our current number and previous number combined can form a number from 10 to 26 inclusive,
        ## we check cases where we pick only one number (i-1) as well as both numbers combined (i-2)
        if (int(s[i-1]) == 1 or (int(s[i-1]) == 2 and int(s[i]) < 7)):
            print('s[i]: ', s[i])
            print('s[i] + s[i-1]', s[i] + s[i-1])
            ways = self.search(s, i-1, memo) + self.search(s, i-2, memo)
        ## if both s[i] and s[i-1] combined create a number greater than 26, then we can only
        ## count individual letters (i-1)
        else:
            ways = self.search(s, i-1, memo)
        memo[i] = ways    
        return ways