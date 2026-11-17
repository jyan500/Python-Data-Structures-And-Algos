"""
https://leetcode.com/problems/search-a-2d-matrix/
Time O(rows * Log(columns)) solution, no additional space

1) For each row, perform a binary search since each row is sorted order
2) If the target value is greater than the last value in the row, we can skip it 
without performing binary search
"""
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """ 
        Because the elements inside each nested array is sorted,
        we can apply binary search
        
        Without needing to apply binary search on each row, you can also
        apply binary search initially to figure out what row to search for

        If the target element is smaller than the first element of that row,
        then we need to search previous rows. If its greater than the last element
        of that row, we need to search later rows.

        Then, once you have the right row where the target is less than the last element,
        but greater than the first element of that row, you can apply binary search again
        to confirm.

        Time Complexity: O(LogN + LogM) = O(Log(N*M))
        Space: O(1)
        """

        start = 0
        end = len(matrix)-1
        designated_row_index = 0
        while (start <= end):
            mid = start + (end - start)//2
            row = matrix[mid]
            # if the target is greater than the last element on this row, search later rows
            if target > row[-1]:
                start = mid + 1
            # if the target is less than the first element on this row, search previous rows
            elif target < row[0]:
                end = mid - 1
            # if the target is range of this row, break and save this index
            elif row[0] <= target <= row[-1]:
                designated_row_index = mid
                break

        l = 0
        r = len(matrix[designated_row_index])-1
        nums = matrix[designated_row_index]
        while (l <= r):
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False


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