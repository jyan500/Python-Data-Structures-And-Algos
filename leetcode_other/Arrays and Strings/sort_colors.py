'''
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
Example 3:

Input: nums = [0]
Output: [0]
Example 4:

Input: nums = [1]
Output: [1]

https://leetcode.com/problems/sort-colors/
https://leetcode.com/problems/sort-colors/discuss/310922/python
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #---------------------------------------------------#
        ## initial solution using O(3N) time and O(N) space

        counter = dict()
        for i in range(len(nums)):
            if (nums[i] in counter):
                counter[nums[i]] += 1
            else:
                counter[nums[i]] = 1
        i = 0
        if (0 in counter):
            for j in range(counter[0]):
                nums[i] = 0
                i+=1
        if (1 in counter):
            for j in range(counter[1]):
                nums[i] = 1
                i+=1
        if (2 in counter):
            for j in range(counter[2]):
                nums[i] = 2
                i+=1
        
        #-----------------------------------------------------#
        ## Swapping solution using O(3N) time and O(1) space
        j = 0
        for i in range(len(nums)):
            if (nums[i] == 0):
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        for i in range(len(nums)):
            if (nums[i] == 1):
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        for i in range(len(nums)):
            if (nums[i]==2):
                nums[j],nums[i]=nums[i],nums[j]
                j+=1
        
        #-------------------------------------------------------#
        ## one pass solution using O(1) space
        ## https://leetcode.com/problems/sort-colors/discuss/310922/python
        
        ## I think the concept behind this solution was that
        ## you keep three pointers, i,j and k, where i, j both start at 0, but k starts at len(nums)-1
        ## i represents the index of the last swapped "zero" in the list (the start of one)
        ## k represents the index of the last swapped "two" in the list, because we want the "twos"
        ## to be stored at the end of the list, whereas for "zeroes", we want that stored in the front
        ## and we want "ones" to be stored between the "zeroes" and "twos"
        
        ## if we see a zero, we will make a swap between i,j elements and increment the i and j index
        ## the reason we increment both is because eventually we want the j index to be greater than i
        ## since we want the "ones" to be ahead of the "zeroes"
        
        ## if we see a two, we will make a swap between j,k elements and decrement k, because the next
        ## two that we find will be the element before.
        
        ## lastly, if the zeroes and twos have already been placed in their proper locations,
        ## then by definition the ones will have already been placed. That's why we don't do a swapping
        ## operation when we see a one, only incrementing j
        i = 0
        j = 0
        k = len(nums)-1
        ## condition j <= k because once all twos have been sorted (or if there are no twos, the end of the list), if j reaches that point, there's no need to perform any more swapping
        while (j <= k):
            if (nums[j] == 0):
                nums[i], nums[j]=nums[j], nums[i]
                i+=1
                j+=1
                # print('i: ', i)
                # print('j: ', j)
            elif (nums[j] == 1):
                # print('j: ', j)
                j+=1
            else:
                nums[j], nums[k]=nums[k], nums[j]
                # print('k: ', k)
                k-=1
        
                
        
       
                
            
                
                
        
            
        