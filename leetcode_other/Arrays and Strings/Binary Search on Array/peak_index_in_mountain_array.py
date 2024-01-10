'''
https://leetcode.com/problems/peak-index-in-a-mountain-array/

Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

 

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1
Example 3:

Input: arr = [0,10,5,2]
Output: 1
Example 4:

Input: arr = [3,4,5,1]
Output: 2
Example 5:

Input: arr = [24,69,100,99,79,78,67,36,26,19]
Output: 2

## Concept:

## Time Complexity : O(LogN)
## Space Complexity : O(1)

## the peak index is the biggest number where the number to 
## the left and right is smaller than the current number

## we can use binary search to figure out if our midpoint number
## is greater than both of the numbers next to it
## if it is, then we've found our peak index
## otherwise, if the number to the left is greater, we need to search the left half ( right = mid.- 1)
## if the number on the right is greater, we need to search the right half (left = mid + 1)

## and we also need to account for two edge cases where the midpoint
## could be at 0 or len(arr) - 1, in that case we'd only compare either the right element (when mid = 0) 
## or the left element (when mid = len(arr)-1)
'''
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
    
        left = 0
        right = len(arr)-1
        while (left <= right):
            mid = (left+right)//2
            prev_element = mid - 1
            next_element = mid + 1
            if (mid == 0):
                if (arr[mid] > arr[next_element]):
                    return mid
                else:
                    left = mid + 1
            elif (mid == len(arr)-1):
                if (arr[mid] > arr[prev_element]):
                    return mid
                else:
                    right = mid - 1
            elif (prev_element >= 0 and next_element < len(arr) and arr[mid] > arr[prev_element] and arr[mid] > arr[next_element]):
                return mid
            elif (arr[mid] < arr[next_element]):
                left = mid + 1
            elif (arr[mid] < arr[prev_element]):
                right = mid - 1
        return -1
    
    '''
    test case #1
    -------------------------
    arr = [0, 10, 5, 2]
    left = 0 
    right = 3
    
    first iteration
    mid = 3//2 = 1
    mid_element = 10
    prev_element = 0, arr[0] = 0
    next_element = 2, arr[2] = 5
    
    peak element has been found, return mid
    
    test case #2
    -------------------------
    arr = [3,4,5,1]
    left = 0
    right = 3

    
    first iteration
    mid = (0+3)//2 = 1
    mid_element = 4
    prev_element = 0, arr[0]=3
    next_element = mid + 1 = 1 + 1 = 2, arr[2] = 5
    
    arr[mid] < arr[next_element], 4 < 5 which is true
    so left = mid + 1 = 1 + 1 = 2
    
    second iteration
    mid = (2+3)//2=2
    mid_element = 5
    
    peek element found, return mid
    
    test case #3
    --------------------------------------
    arr = [24,69,100,99,79,78,67,36,26,19]
    left = 0
    right = 10 - 1 = 9
    
    first iteration
    mid = (0+9)//2 = 4
    mid_element = arr[4] = 79
    
    prev_element = mid - 1 = 3, arr[3] = 99
    arr[mid] < prev_element, 79 < 99 which is true
    right = mid - 1 = 4 - 1 = 3
    
    second iteration
    left = 0
    right = 3
    mid = (0+3)//2 = 1
    prev_element = mid - 1 = 0, arr[0] = 24
    next_element = mid + 1 = 2, arr[2] = 100
    
    arr[mid] < next_element, 69 < 100, which is true
    left = mid + 1 = 1 + 1 = 2
    
    third iteration
    left = 2
    right = 3
    mid = (3+2)//2 = 2
    prev_element = 2-1=1, arr[1] = 69
    next_element = mid + 1 = 2 + 1 = 3, arr[3] = 99
    
    arr[mid] > prev_element and arr[mid] > next_element, so peak has been found
    return mid
    
    test case #4
    -------------------------
    arr = [10,9,8,7,6]
    left = 0 
    right = 5 - 1 = 4
    
    first iteration
    mid = (0+4)//2=2, mid_element = arr[2] = 8
    prev_element = mid - 1 = 2 - 1 = 1, arr[1] = 9
    next_elemenet = mid + 1 = 2 + 1 = 3, arr[3]= 7
    
    arr[mid] < arr[prev_element], 8 < 9, which is true
    right = mid - 1 = 1
    
    second iteration
    mid = (0+1)//2 = 0
    prev_element = -1, we're not going to compare arr[mid] with arr[prev_element]
    in this case because prev_element < 0
    next_element = mid + 1 = 0 + 1 = 1, arr[1] = 9
    10 > 9, and since we're not comparing a prev element,
    
    test case #5
    [3,5,3,2,0]
    left = 0
    right = 5 - 1 = 4
    first iteration
    mid = (0+4)//2 = 2, mid_element = arr[2] = 3
    prev_element = 2-1=1, arr[1] = 5
    next_element = 2+1=3, arr[3] = 2
    arr[mid] < arr[prev_element], 3 < 5, 
    
    right = mid - 1, 2 - 1 = 1
    
    second iteration
    mid = (0+1)//2 = 0
    
    
    
    '''
            