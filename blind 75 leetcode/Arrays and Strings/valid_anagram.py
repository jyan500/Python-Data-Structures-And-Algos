'''
https://leetcode.com/problems/valid-anagram/
O(N) time, O(1) space (despite using a hashmap, the table size remains constant)
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict()
        if (len(s) != len(t)):
            return False
        for i in range(len(s)):
            if (map1.get(s[i]) != None):
                map1[s[i]] += 1
            else:
                map1[s[i]] = 1
        for j in range(len(t)):
            if (map1.get(t[j]) != None):
                map1[t[j]] -= 1
            else:
                return False
        for key in map1:
            if (map1[key] < 0):
                return False
        return True
        