'''
https://leetcode.com/problems/russian-doll-envelopes/

Test cases:
[[5,4],[6,4],[6,7],[2,3]]
[[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]
'''

class Solution:
	## 7/2/2021
	## My first approach , using Top Down Memoization Approach
	## this is still TLE despite the memoization
	## there's still quite a bit of un-needed recursive calls
	## I think intuitively, sorting the list by the greatest width, and then the height
	## should help, but we'd need to find the right point to "stop iterating" and realize
	## that we've found the max total already and not continually use smaller envelopes (thus creating smaller totals)
	## but not sure what that is right now

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        ## things that we know:
        ## if a envelope a fits in envelope b...
        ## if envelope b fits in envelope c, we know that envelope a also fits in envelope c
        
        ## generate all different combinations where one envelope fits in the other
        ## and if we know that a certain envelope A fits within larger envelope B,
        ## all the envelopes that fit in A will also fit in B as well.
        
        ## recursion (top down)
        ## pick an envelope and 
        ## progressively find smaller and smaller envelopes to fit into
        ## the "total" represents the amount of smaller envelopes we've found so far (including the current envelope)
        ## we just need to keep track of the max we have found
        
        ## [6,7]
        ## [6,7] can fit [5,4] or [2,3], recursion tree picks [5,4]
        ## [5,4] can fit [2,3]
        ## [2,3] can't fit anything else
        ## backtrack to [5,4] ... , [5,4] can't fit anything else, backtrack into [6,7]
        ## pick the first envelope in our list

        ## 
        memo = dict()
        if (len(envelopes) == 1):
            return 1
        ## Sorting should make the algorithm faster
        ## by cutting down on unnecessary calls where the max is no longer being updated
        ## sorted_envelopes = sorted(envelopes, key = lambda envelope: [envelope[0], envelope[1]], reverse = True)
        sorted_envelopes = envelopes
        max_total = 1
        for i in range(len(sorted_envelopes)):
            print('chosen envelope at the top level: ', sorted_envelopes[i])
            max_total = max(max_total, self.search(sorted_envelopes[0:i]+sorted_envelopes[i+1:], sorted_envelopes[i], memo))
        return max_total
    
    def search(self, envelopes, cur, memo) -> int:
        ## first base case: no more envelopes to pick
        c = tuple(cur)
        if (c in memo):
            return memo[c]
        if (not envelopes):
            ## print('no more envelopes')
            return 1
        ## someway to keep track of how many smaller envelopes that we've found
        total = 1
        for j in range(len(envelopes)):
            ## print('is envelope small: ', envelopes[j], cur, self.isEnvelopeSmaller(envelopes[j], cur))
            if self.isEnvelopeSmaller(envelopes[j], cur):
                ## print('chosen envelope: ', envelopes[j])
                ## we want to find the max between our current total and the number of smaller envelopes that we've found
                amt = 1 + self.search(envelopes[0: j] + envelopes[j+1:], envelopes[j], memo)
                # print('amt: ', amt)
                
                total = max(total, amt)
                
                # print('memo: ', memo)
                # print('current total: ', total)
        ## we can memoize 
        memo[c] = total
        return total

    def isEnvelopeSmaller(self, e1, e2):
        e1_width, e1_height = e1
        e2_width, e2_height = e2
        return (e1_width < e2_width and e1_height < e2_height)
