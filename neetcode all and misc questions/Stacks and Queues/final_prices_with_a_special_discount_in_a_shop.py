class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        """
        https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/
        
        keep a stack where we keep track of the index, and also check whether
        the current element is less than or equal to the top of the stack. If so,
        that means the top of the stack should be receiving a discount,
        so we pop out of the stack and store in an intermediate result array for that index

        this is a similar concept to the daily temperatures problem

        Time: O(N)
        Space: O(N)
        """
        res = prices.copy()
        stack = []
        for i in range(len(prices)):
            # if the current price <= top of the stack's price, the top of the stack should receive a discount
            # so get the original index of the top of the stack, and then set it in the res array to the discount by subtracting
            # the top of the stack price from the current price 
            while (len(stack) > 0 and prices[i] <= stack[-1][1]):
                index, price = stack.pop()
                res[index] = price - prices[i]
            stack.append((i, prices[i]))
        return res