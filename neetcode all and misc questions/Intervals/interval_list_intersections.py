"""
Time: O(N)
Space: O(1)

Approach: Similar to merge sorted lists, using two pointers.
The trick is that whenever the end time A < end time B, you shift the pointer for A,
as you want to check the next greater end time. 

Then, there's four cases to handle when the intervals intersect, which can be seen in the code comments.

Revisited on 6/23/2025 with the same solution
"""
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        l = 0
        r = 0
        res = []
        while (l < len(firstList) and r < len(secondList)):
            start1, end1 = firstList[l]
            start2, end2 = secondList[r]
            """ 
            get the intersection between the two lists
            There's 4 different cases
            
            A -----
            B  ---
            
            B interval exists inside of A, so we just return B
            
            A  ---
            B -----
            
            A interval exists inside of B, so just return A
            
            A ----
            B     ----
            
            A ends as soon as B starts, so we just return the end of A and the beginning of B
            
            A ----
            B   ----
            
            There's a mismatch, where either A's end time > B's start time, or B's end time > A's start time
            """
            # B exists inside of A, just return B
            element = []
            if start2 >= start1 and end2 <= end1:
                element = [start2, end2]
            # A exists inside of B, just return A
            elif start1 >= start2 and end1 <= end2:
                element = [start1, end1]
            # A ends when B starts or B ends when A starts
            elif start1 == end2 or start2 == end1:
                if (start1 == end2):   
                    element = [start1, start1]
                elif (start2 == end1):
                    element = [start2, start2]
            # mismatch
            elif (start1 < start2 and end1 > start2) or (start2 < start1 and end2 > start1):
                element = [max(start1, start2), min(end1, end2)]
            # if there's no intersection, ignore this case
            if len(element) > 0:
                res.append(element)
            # if the end1 < end2, similar to merge sorted lists, only increment the left pointer
            # to compare the next greater end time
            if end1 < end2:
                l += 1
            else:
                r += 1 
        return res
                