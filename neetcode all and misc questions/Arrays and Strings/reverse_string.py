'''
Write a function that reverses a string. The input string is given as an array of characters s.

 

Example 1:

Input: s = ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: s = ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

Concept:
Time O(N), Space O(1)
keep two pointers, beginning and end
swap the values located at the two pointers as you move the two pointers towards each other
this will reverse the array in place

Revisited 2/25/2025

'''
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        j = len(s)-1
        while (i <= j):
            s[i],s[j] = s[j],s[i]
            i+=1
            j-=1
        