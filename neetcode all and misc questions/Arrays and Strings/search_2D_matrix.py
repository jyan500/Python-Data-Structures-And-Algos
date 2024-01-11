"""
https://leetcode.com/problems/search-a-2d-matrix/
Time O(rows * Log(columns)) solution, no additional space

1) For each row, perform a binary search since each row is sorted order
2) If the target value is greater than the last value in the row, we can skip it 
without performing binary search
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearch(left, right, row, target):          
            mid = left + (right - left)//2
            if row[mid] == target:
                return True
            if left >= right:
                return False
            if target > row[mid]:
                return binarySearch(mid+1, right, row, target)
            if target < row[mid]:
                return binarySearch(left, mid-1, row, target)
            
        for i in range(len(matrix)):
            if target <= matrix[i][-1]:
                if binarySearch(0, len(matrix[i])-1, matrix[i], target):
                    return True
        return False