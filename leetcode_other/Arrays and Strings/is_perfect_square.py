"""
https://leetcode.com/problems/valid-perfect-square/

Binary Search, where we search the space from
1 ... num,
and for each midpoint, we check if the mid * mid is equal to our target
if it's less than our target, we search the right half
if it's greater, we search the left half

O(LogN)
"""
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left = 1
        right = num
        def search(left, right, num):
            mid = left + (right-left)//2
            if mid * mid == num:
                return True
            if left >= right:
                return False
            elif mid * mid < num:
                return search(mid+1, right, num)
            elif mid * mid > num:
                return search(left, mid, num)
        return search(left, right, num)