'''
https://leetcode.com/problems/decode-ways/
https://www.youtube.com/watch?v=W4rYz-kd-cY&list=PLQdWvigIOnscYtuD1UesE2IazI1erKh-W&index=48&ab_channel=Knapsak
'''
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