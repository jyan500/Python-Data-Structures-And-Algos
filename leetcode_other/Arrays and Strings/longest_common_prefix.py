'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 
Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        Concept:
        Time complexity: O(length of the shortest string), because this is essentially a "horizontal" scan, we are looking at the first
        index of each string, then the second, then the third, etc until we hit the length of the shortest string in our list. 
        Space Complexity: O(1)
        compare the indices of each string in the list, we can only go as far
        as the length of the shortest string in our list to avoid going out of bounds
        
        iterate by length of the shortest string (i), and then through the list of strings (j), indexing by j, i
        set the current prefix to be whatever string indices we're on
        if after the first string, the prefix is no longer equal, just return the longest
        common prefix we've built so far
        otherwise, add the current prefix to the longest common prefix
        '''
        longest_common_prefix = ''
       
        length_shortest_string = float('inf')
        for i in range(len(strs)):
            length_shortest_string = min(length_shortest_string, len(strs[i])) 
        for i in range(length_shortest_string):
            cur_prefix = ''
            for j in range(len(strs)):
                if (j != 0 and strs[j][i] != cur_prefix):
                        return longest_common_prefix
                cur_prefix = strs[j][i]
            longest_common_prefix += cur_prefix
                
            
        return longest_common_prefix
                
            
                
        