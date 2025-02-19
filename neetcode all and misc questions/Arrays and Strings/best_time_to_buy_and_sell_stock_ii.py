class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Revisited on 2/19/2025 with the same solution
        https://www.youtube.com/watch?v=3SJ3pUkPQMc&ab_channel=NeetCode
        Concept:
        1) As seen in the neetcode vid, we only turn a profit when 
        going from a lower to a higher price.
        2) Loop through the array and see if the previous price is higher, if so
        add the difference between the current and previous price to our total profit
        """
        total = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
        return total