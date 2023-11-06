"""
https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
"""
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # for i in range(len(arr)):
        #     if len(arr[i+1:]):
        #         arr[i] = max(arr[i+1: ])
        #     else:
        #         arr[i] = -1
        # return arr
        
        """
        looping from the end, we can keep track of the current max
        this is more efficient than going from the front
        """
        curMax = float("-inf")
        for i in range(len(arr)-1,-1,-1):
            prev = arr[i]
            arr[i] = -1 if i == len(arr) - 1 else curMax
            curMax = max(prev, curMax)
        return arr