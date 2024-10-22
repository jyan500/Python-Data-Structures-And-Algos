"""
https://leetcode.com/problems/buy-two-chocolates/
"""
class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        cur = money - sum(prices[:2])
        return cur if cur >= 0 else money
            
