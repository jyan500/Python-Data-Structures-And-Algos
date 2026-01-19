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
"""Revisited 1/19/2026 with the solution below, not the most pythonic """
"""
Revisited 7/28/2023
"pythonic" solution
1) use zip to get a list of tuples of each character based on index 
it uses the * operator in python to unpack a list as parameters for the function
i.e a = ["car", "cired", "core"] -> zip(*a) evaluates to -> zip("car", "cired", "core")
-> [("c", "c", "c"), ("a", "i", "o"), ("r", "r", "r")]
Note there's only three entries because the shortest string is only length 3

If each character in the tuple is the same, that means they share the same prefix
If a character is not the same, we end the loop early

O(N^2) time complexity, because the len(set(zipped)) is O(N) operation, for each tuple of N characters.
In the worst case, each string is the same and we end up checking the whole length of it
O(N^2 space) for the zip(*strs), since it's a tuple of each character in all strings? 
it might also just be the length of the prefix string
"""
class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        for zipped in zip(*strs):
            if len(set(zipped)) == 1:
                prefix += zipped[0]
            else:
                break
       
        return prefix

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
                
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        find the shortest word in the list to get the length
        loop through all words, until the length of the shortest word,
        and comparing the prefixes
        """
        shortestLength = float("inf")
        shortestWord = ""
        for i in range(len(strs)):
            if len(strs[i]) < shortestLength:
                shortestWord = strs[i]
                shortestLength = len(strs[i])
        
        i = 0
        prefix = ""
        while (i < len(shortestWord)):
            flag = True
            curLetter = strs[0][i]
            for j in range(1, len(strs)):
                if strs[j][i] != strs[j-1][i]:
                    flag = False
                    break
                else:
                    curLetter = strs[j][i]
            if flag:
                prefix += curLetter
            # if the prefixes don't match in one instance, break out of the whole process
            else:
                break
            i += 1
        return prefix
            
            
                
        