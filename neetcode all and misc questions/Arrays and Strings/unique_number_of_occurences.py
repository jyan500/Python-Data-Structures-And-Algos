'''
Given an array of integers arr, write a function that returns true if and only if the number of occurrences of each value in the array is unique.

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true

'''
class Solution:
	## O(N) time, O(N) space
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = dict()
        ## create a counter to map the array element to number of occurences
        for i in range(len(arr)):
            if (arr[i] in counter):
                counter[arr[i]] += 1
            else:
                counter[arr[i]] = 1
        ## since the question asks for unique number of occurences of each element in the array
        ## if we convert our counts into a set, it will remove the duplicate number of occurences
        ## so just check if the length of the original list and the length of the new set is the same
        return len(counter.values()) == len(set(counter.values()))
    
        '''
        counter = dict()
        [1,2,2,1,1,3]
        after iteration, counter = {1:3,2:2,3:1}
        counter.values() = [3,2,1], set(counter) == {3,2,1}
        
        '''