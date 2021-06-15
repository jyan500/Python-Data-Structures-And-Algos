'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
https://leetcode.com/problems/group-anagrams/

'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = dict()
        for i in range(len(strs)):
            ## sorting the string each time allows us to make a key that we
            ## can compare each string to
            ## since if two sorted strings are the same, they are anagrams
            key = "".join(sorted(list(strs[i])))
            if (lookup.get(key) != None):
                lookup[key].append(strs[i])
            else:
                lookup[key] = [strs[i]]
        result = []
        ## append the list for each key to result
        for l in lookup.values():
            result.append(l)
        return result
    
