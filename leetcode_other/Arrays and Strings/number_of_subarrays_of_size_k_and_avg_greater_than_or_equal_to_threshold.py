"""
https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/

Key Concepts:
Sliding Window

Time Complexity: O(N)
Space: O(1)
"""
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        """
        initialize the left and right pointers to be of length k,
        and the current total to be l:r (but not including the value of r,
        since we will add that value inside the while loop)
        """
        l = 0 
        r = k - 1
        res = 0
      
        curTotal = sum(arr[l:r])
        while (r < len(arr)):
            """
            add the very last element of the window and calculate the average
            if the average exceeds the threshold, increment the result.
            
            Shift the window by decrementing the current total by the left most
            value, and then incrementing both the left and right pointers
            """   
            curTotal += arr[r]
            avg = curTotal/k
            if avg >= threshold:
                res += 1
            curTotal -= arr[l]
            l += 1
            r += 1        
        return res