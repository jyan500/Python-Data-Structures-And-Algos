'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.

https://leetcode.com/problems/longest-continuous-increasing-subsequence/
'''
class Solution:
    '''
    Time: O(N), loops through the list once
    Space: O(1), no extra memory
    
    Concept:
    1. Two pointers
    and keep track of current distance and max distance
    one cur, one previous (i, j)
    2. if the value at cur is greater than value at previous,
    we increase distance, and increase both cur and previous
    
    3. however, if value at cur == value at previous or value at cur < value at previous
    we will find the max distance based on our current distance calculated
    we need to set previous equal to cur now, and set cur + 1, so its ahead of previous
    
    we don't need to go backwards to index 1 because that would just result in the same,
    i.e [1,3,5,4,7]
    if i = 3 and j = 2, we would set j = 3 and i = 4,
    there's no need to set i back to 1 and j back to 1 (starting from 3), because once we hit 4 we would just
    be hitting the same issue where there's a non-continuous element (4), plus it'd just be a shorter subarray
    so there's no need.
    
    4. at the end, because the loop breaks, we'll need to re-calculate the max between curr distance and max
    to find the answer
    
    
    
    '''
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        i = 0
        j = 0
        max_dist = float('-inf')
        dist = 1
        while (i < len(nums)):
            if (nums[i] > nums[j]):
                i += 1
                j += 1
                dist += 1
            else:
                max_dist = max(dist, max_dist)  
                j = i
                i+=1
                dist = 1
        return max(max_dist, dist)
                
                
            
        '''
        test case #1
        [-3,-2,-1,4,-2,5,6]
        i = 0
        j = 0
        dist = 1
        -3 > -3, answer is no
        max_dist = max(dist, max_dist) = max(1, -inf)
        max_dist = 1
        
        i = 1
        j = 0
        -2 > -3, increment dist by 1, i += 1, j+=1
        dist = 2
        
        i = 2
        j = 1
        -1 > -2, increment dist by 1, i += 1, j += 1
        dist = 3
        
        i = 3
        j = 2
        4 > -1, increment dist by 1, i+=1, j+= 1
        dist = 4
        
        i =4
        j =3
        -2 < 4, answer is no
        max_dist = max(dist, max_dist) = 4
        max_dist = 4
        j = 4
        i = 5
        dist = 1
        
        i = 5
        j = 4
        5 > -2, increment dist by 1, i += 1, j += 1
        dist = 2
        
        i = 6
        j = 5
        6 > 5, increment dist by 1, i += 1, j += 1
        
        i = 7, so loop breaks
        
        re-calculate the max between dist and max dist
        max(4,3) = 4
        result = 4
        
        test case #2
        [1,3,5,4,7]
        i = 0
        j = 0
        dist = 1
        
        i = 1
        j = 0
        3 > 1, dist += 1, i += 1,j +=1
        dist = 2
        
        i = 2
        j = 1
        5 > 3, dist += 1, i += 1, j+=1
        dist = 3
        
        i = 3
        j = 2
        4 < 5, answer is no
        max_dist = max(dist, max_dist) = max(3,float(-inf))= 3
       
        j = 3
        i = 4
        dist = 1
        
        i = 4
        j = 3
        
        7 > 4, dist += 1, dist = 2
        
        max(2,3) = 3
        
        
        
        '''