'''
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?

Example 1:

Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
Example 2:

Input: nums = [0,1]
Output: 2
Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
Example 3:

Input: nums = [9,6,4,2,3,5,7,0,1]
Output: 8
Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
Example 4:

Input: nums = [0]
Output: 1
Explanation: n = 1 since there is 1 number, so all numbers are in the range [0,1]. 1 is the missing number in the range since it does not appear in nums.

Constraints:

n == nums.length
1 <= n <= 104
0 <= nums[i] <= n
All the numbers of nums are unique

https://leetcode.com/problems/missing-number/

O(N) time and O(N) space approach
Just keep a set of all the nums for O(1) lookup in each iteration
start an i value at 0, and keep incrementing until we find the i
value that is not in our nums set

'''
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ## O(N) time O(N) space
        s = set(nums)
        i = 0
        while (i <= len(nums)):
            if (i not in s):
                return i
            i+=1
        return -1
    
        ## The O(1) solution uses the gauss formula or XOR bit solution 
        ## seen here: https://leetcode.com/problems/missing-number/solution/
        
        
    
    
    '''
    test case
    nums = [3,0,1]
    i = 0
    s = {3,0,1}
    len(nums) = 3
    
    i = 1
    i = 2
    '''
        