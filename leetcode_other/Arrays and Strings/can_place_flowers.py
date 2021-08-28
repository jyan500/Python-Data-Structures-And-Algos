'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

https://leetcode.com/problems/can-place-flowers/
'''
class Solution:
    ## initial:
    ## time complexity: O(2N) 
    ## space complexity: O(1)
    ## concept:
    ## first pass is to block out adjacent indices by setting them to '#'
    ## second pass is to start planting flowers at the remaining spots in the array with value '0'
    ## also increment every time a flower can be successfully planted
    ## return if the number of flowers planted greater than or equal to requirement
    
    ## optimized: 
    ## time complexity: O(N)
    ## space complexity: O(1)
    ## combine the concepts of the previous solution into a single pass
    ## for each value 0 found in the flowerbed, check if its adjacent spots are also zero
    ## if so, then set the array value to 1 
    ## this works because if we encounter a case where we have two zeroes adjacent,
    ## after the first flower is planted, we can't plant the second since we'll see the value 
    ## previously has already been planted
    
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        count = 0
        for i in range(N):
            if (flowerbed[i] == 0):
                ## if we're at the beginning of the array, we only need to check flowerbed[i + 1] == 0
                ## if we're at the end of the array, we only need to check flowerbed[i - 1] == 0
                ## anywhere in between, the logic will check flowerbed[i-1] == 0 and flowerbed[i+1] == 0
                if ((i == 0 or flowerbed[i-1]==0) and (i == N-1 or flowerbed[i+1]==0)):
                    flowerbed[i] = 1
                    count += 1
        return count >= n
    
    ## initial solution with 2 passes:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        for i in range(N):
            if (flowerbed[i] == 1):
                if (i - 1 >= 0):
                    flowerbed[i-1]='#'
                if (i + 1 < N):
                    flowerbed[i+1]='#'
        num_places = 0
        for i in range(N):
            if (flowerbed[i] == 0):
                flowerbed[i] = 1
                if (i - 1 >= 0):
                    flowerbed[i-1] = '#'
                if (i + 1 < N):
                    flowerbed[i+1] = '#'
                num_places += 1
        return num_places >= n
    
    
       