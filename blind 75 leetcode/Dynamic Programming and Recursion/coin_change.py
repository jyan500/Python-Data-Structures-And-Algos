'''
https://leetcode.com/problems/coin-change/submissions/
Top-Down Solution: https://www.youtube.com/watch?v=Kf_M7RdHr1M&ab_channel=TusharRoy-CodingMadeSimple	
Bottom Up Solution: https://www.youtube.com/watch?v=H9bfqozjoqs&t=3s&ab_channel=NeetCode

The Top Down Solution's Time Complexity is
O(total value * total amount of coins)
'''
class Solution:
   	## bottom up solution 
    def coinChangeBottomUp(self, coins: List[int], amount: int)->int:
        dp = [float(inf)] * (amount + 1)
        ## number of coins to make 0 is 0 coins, so we initialize this value
        dp[0] = 0
        ## start from 0
        ## minimum ways to make 0?, to make 1? so on... until amount + 1
        ## use the previous result stored in the DP array to calculate the new result
        for i in range(1, amount + 1):
            ## using each coin, what's the minimum amount of coins we can make at this amount i?
            for c in coins:
                ## if the coin value is less than or equal to the amount, we know that 
                ## this coin can contribute to the minimum amount of coins,
                ## if the coin value is greater than the value, than it can't contribute so we skip 
                if c <= i:
                    dp[i] = min(dp[i], 1 + dp[i - c])
        if dp[amount] != float(inf):
            return dp[amount]
        else:
            return -1
    ## top down DP solution
    ## where we save the result within the memoization hash map
    ## we start with the total amount of coins we want to create
    ## and we start subtracting different coins to get a remaining amount
    ## then we perform recursion on this remaining amount 
    def coinChange(self, coins: List[int], amount: int) -> int:
        ## dfs/backtracking solution
        memo = dict()
        res = self.memoizeRecur(coins, amount, memo)
        if (res == float(inf)):
            return -1
        else:
            return res
       
    
    def memoizeRecur(self, coins, amount, memo):
        ## if total is 0, then there is nothing to do, return 0
        if (amount == 0):
            return 0
        ## if map contains the result, then we calculated it before. return this value
        if memo.get(amount) != None:
            return memo.get(amount)
        ## iterate through all coins and see which one gives best result
        min_val = float(inf)
        for i in range(len(coins)):
            ## value of coin is greater than the amount we are looking for
            if (coins[i] > amount):
                continue
            
            ## recur with amount - coins[i] as the new amount
            val = self.memoizeRecur(coins, amount - coins[i], memo)
            
            ## if val we get from picking coins[i] as first coin for current amount is less
            ## than the value found, make it the minimum
            if (val < min_val):
                min_val = val
        ## update the minval by adding 1 if it needs to be updated
        ## we add one because we're taking 1 coin and adding it onto the memoization total
        ## which would be the total number of coins
        if (min_val != float(inf)):
            min_val += 1
        
        ## memoize the current amount
        memo[amount] = min_val
        return min_val
            
        